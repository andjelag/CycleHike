from flask import Flask, request, Response, json
from flask_cors import CORS, cross_origin
from configuration import Configuration
from models import database, Route, User, UserRole, UserRoute, Peak, RoutePeak
from flask_jwt_extended import JWTManager, get_jwt_identity, create_access_token
from sqlalchemy import and_, or_
from datetime import datetime

application = Flask(__name__)
application.config.from_object(Configuration)
cors = CORS(application)

jwt = JWTManager(application)


@application.route("/", methods=["GET", "POST"])
@cross_origin()
def index():
    return "<h1>Hello world!</h1>"

################################ User #################################
@ application.route("/getAllUsers", methods=["GET"])
def getAllUsers():
    users = User.query.all()
    users = [{
            "id": user.id,
            "forename": user.forename,
            "surname": user.surname,
            "email": user.email,
            "phone": user.phone,
            "photo": user.photo,
            "role": str(user.roles[0]),
            "routes": [{
                    "id": route.id,
                    "name": route.name,
                    "capacity": route.capacity,
                    "capacityLeft": route.capacityLeft,
                    "date": route.date,
                    "summary": route.summary,
                    "description": route.description,
                    "gpx": route.gpx,
                    "photo": route.photo,
                    "price":route.price,
                    "peaks": [{
                        "name": peak.name,
                        "elevation": peak.elevation
                    } for peak in route.peaks]
                } for route in user.routes],
            "status":user.status
        } for user in users if str(user.roles[0])=="user"]
    return Response(json.dumps(users), status=200)


@ application.route("/getUser", methods=["POST"])
def getUser():
    id = request.json.get("id", None)
    user = User.query.filter(User.id == id).first()
    user = {
            "id": user.id,
            "forename": user.forename,
            "surname": user.surname,
            "email": user.email,
            "phone": user.phone,
            "photo": user.photo,
            "role": str(user.roles[0]),
            "routes": [{
                    "id": route.id,
                    "name": route.name,
                    "capacity": route.capacity,
                    "capacityLeft": route.capacityLeft,
                    "date": route.date,
                    "summary": route.summary,
                    "description": route.description,
                    "gpx": route.gpx,
                    "photo": route.photo,
                    "price":route.price,
                    "peaks": [{
                        "name": peak.name,
                        "elevation": peak.elevation
                    } for peak in route.peaks]
                } for route in user.routes],
            "status":user.status
        }
    return Response(json.dumps(user), status=200)


@application.route("/approveUser", methods=["POST"])
def approveUser():
    id = request.json.get("id", None)

    user = User.query.filter(User.id == id).first()
    user.status = "A"
    database.session.commit()

    return Response(json.dumps({"message":"Ok"}), status=200)


@application.route("/deactivateUser", methods=["POST"])
def deactivateUser():
    id = request.json.get("id", None)
    
    user = User.query.filter(User.id == id).first()
    user.status = "U"
    database.session.commit()

    return Response(json.dumps({"message":"Ok"}), status=200)


@application.route("/updateUserInfo", methods=["POST"])
def updateUserInfo():
    forename = request.json.get("forename", "")
    surname = request.json.get("surname", "")
    phone = request.json.get("phone", "")
    photo = request.json.get("photo", "")

    forenameEmpty = len(forename) == 0
    surnameEmpty = len(surname) == 0
    phoneEmpty = len(phone) == 0
    photoEmpty = len(photo) == 0

    if forenameEmpty or surnameEmpty or phoneEmpty or photoEmpty:
        return Response(json.dumps({"message": "Fields missing."}), status=200)
    
    id = request.json.get("id", None)
    user = User.query.filter(User.id == id).first()
    if user is None:
        return Response(json.dumps({"message": "User doesn't exist."}), status=200)


    user.forename = forename
    user.surname = surname
    user.phone = phone
    user.photo = photo
    database.session.commit()

    return Response(json.dumps({"message":"Ok"}), status=200)


@application.route("/updateUserPassword", methods=["POST"])
def updateUserPassword():
    oldPassword = request.json.get("oldPassword", "")
    newPassword = request.json.get("newPassword", "")

    oldPasswordEmpty = len(oldPassword) == 0
    newPasswordEmpty = len(newPassword) == 0

    if oldPasswordEmpty or newPasswordEmpty:
        return Response(json.dumps({"message": "Fields missing."}), status=200)
    
    id = request.json.get("id", None)
    user = User.query.filter(and_(User.id == id, User.password == oldPassword)).first()
    if user is None:
        return Response(json.dumps({"message": "Wrong password."}), status=200)


    user.password = newPassword
    database.session.commit()

    return Response(json.dumps({"message":"Ok"}), status=200)


################################ Login & Register  #################################
@ application.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", "")
    password = request.json.get("password", "")

    emailEmpty = len(email) == 0
    passwordEmpty = len(password) == 0

    if emailEmpty:
        return Response(json.dumps({"message": "Field email is missing."}), status=200)
    if passwordEmpty:
        return Response(json.dumps({"message": "Field password is missing."}), status=200)

    user = User.query.filter(
        and_(
            User.email == email,
            User.password == password
        )
    ).first()

    if not user:
        return Response(json.dumps({"message": "Invalid credentials."}), status=200)

    additionalClaims = {
        "email": user.email,
        "roles": [str(role) for role in user.roles]
    }
    accessToken = create_access_token(
        identity=user.id, additional_claims=additionalClaims)

    return Response(json.dumps({"accessToken": accessToken, "userId": user.id, "expiresIn": str(application.config["JWT_ACCESS_TOKEN_EXPIRES"])}), status=200)

@application.route("/register", methods=["POST"])
def register():
    email = request.json.get("email", "")
    password = request.json.get("password", "")
    forename = request.json.get("forename", "")
    surname = request.json.get("surname", "")
    phone = request.json.get("phone", "")
    photo = request.json.get("photo", "")

    emailEmpty = len(email) == 0
    passwordEmpty = len(password) == 0
    forenameEmpty = len(forename) == 0
    surnameEmpty = len(surname) == 0
    phoneEmpty = len(phone) == 0
    photoEmpty = len(photo) == 0

    if forenameEmpty or surnameEmpty or emailEmpty or passwordEmpty or phoneEmpty or photoEmpty:
        return Response(json.dumps({"message": "Fields missing."}), status=200)
    userExists = User.query.filter(User.email == email).first() is not None
    if userExists:
        return Response(json.dumps({"message": "Email already exists."}), status=200)

    user = User(email=email, password=password,
                    forename=forename, surname=surname, phone=phone, photo=photo, status='U')
    database.session.add(user)
    database.session.commit()

    userRole = UserRole(userId=user.id, roleId=2)
    database.session.add(userRole)
    database.session.commit()

    return Response(json.dumps({"message":"Ok"}), status=200)

################################ Routes ################################
@application.route("/routes/getRouteById", methods=["POST"])
@cross_origin()
def getRouteById():
    id = request.json.get("id", None)
    route = Route.query.filter(Route.id == id).first()
    route = {
            "id": route.id,
            "name": route.name,
            "capacity": route.capacity,
            "capacityLeft": route.capacityLeft,
            "date": route.date,
            "summary": route.summary,
            "description": route.description,
            "gpx": route.gpx,
            "photo": route.photo,
            "price":route.price,
            "peaks": [{
                "name": peak.name,
                "elevation": peak.elevation
            } for peak in route.peaks]
        }
    return Response(json.dumps(route), status=200)


@application.route("/routes/cancelRoute",  methods=['POST'])
def cancelRoute():
    id = request.json.get("id", None)
    route = Route.query.filter(Route.id == id).first()

    database.session.delete(route)
    database.session.commit()

    return Response(json.dumps({"message":"Ok"}), status=200)


@application.route("/routes/getAllRoutes", methods=["GET", "POST"])
@cross_origin()
def getAllRoutes():
    routes = Route.query.all()
    routes = [
        {
            "id": route.id,
            "name": route.name,
            "capacity": route.capacity,
            "capacityLeft": route.capacityLeft,
            "date": route.date,
            "summary": route.summary,
            "description": route.description,
            "gpx": route.gpx,
            "photo": route.photo,
            "price":route.price,
            "peaks": [{
                "name": peak.name,
                "elevation": peak.elevation
            } for peak in route.peaks]
        }
        for route in routes
    ]
    return Response(json.dumps(routes), status=200)


@application.route("/routes/getRoutes", methods=["POST"])
def getRoutes():
    searchText = request.json.get("searchText", None)
    routes = Route.query.filter(
        or_(Route.name.contains(searchText), Route.summary.contains(searchText))
    ).all()
    routes = [
        {
            "id": route.id,
            "name": route.name,
            "capacity": route.capacity,
            "capacityLeft": route.capacityLeft,
            "date": route.date,
            "summary": route.summary,
            "description": route.description,
            "gpx": route.gpx,
            "photo":route.photo,
            "price":route.price,
            "peaks": [{
                "name": peak.name,
                "elevation": peak.elevation
            } for peak in route.peaks]
        }
        for route in routes
    ]
    return Response(json.dumps(routes), status=200)


@application.route("/routes/addRoute", methods=["POST"])
def addRoute():
    name = request.json.get("name", None)
    capacity = request.json.get("capacity", None)
    capacityLeft = capacity
    date = request.json.get("date", None)
    summary = request.json.get("summary", None)
    description = request.json.get("description", None)
    gpx = request.json.get("gpx", None)
    photo = request.json.get("photo", None)
    price = request.json.get("price", None)
    peaks = request.json.get("peaks", None)
    
    if name is not None and capacity is not None and date is not None and summary is not None and description is not None and gpx is not None and photo is not None and price is not None:        
        route = Route(name=name, capacity = capacity, capacityLeft = capacityLeft, date = date, summary = summary, description = description, gpx = gpx, photo = photo, price = price)
        database.session.add(route)
        database.session.commit()
        for peak in peaks:
            peakFromDatabase = Peak.query.filter(Peak.name == peak['name']).first()
            if peakFromDatabase is not None:
                routePeakInDatabase = RoutePeak.query.filter(and_(RoutePeak.routeId == route.id, RoutePeak.peakId == peakFromDatabase.id)).first()
                if routePeakInDatabase is None:
                    routePeak = RoutePeak(routeId = route.id, peakId = peakFromDatabase.id)
                    database.session.add(routePeak)
                    database.session.commit()
            else:
                newPeak = Peak(name=peak['name'], elevation=peak['elevation'])
                database.session.add(newPeak)
                database.session.commit()
                routePeak = RoutePeak(routeId = route.id, peakId = newPeak.id)
                database.session.add(routePeak)
                database.session.commit()


        return Response(json.dumps({"message":"Ok"}), status=200)

    return Response(json.dumps({"message":"Error"}), status=200)


@application.route("/routes/editRoute", methods=["POST"])
def editRoute():
    id = request.json.get("id", None)
    name = request.json.get("name", None)
    capacity = request.json.get("capacity", None)
    date = request.json.get("date", None)
    summary = request.json.get("summary", None)
    description = request.json.get("description", None)
    gpx = request.json.get("gpx", None)
    photo = request.json.get("photo", None)
    price = request.json.get("price", None)
    peaks = request.json.get("peaks", None)

    if name is not None and capacity is not None and date is not None and summary is not None and description is not None and gpx is not None and photo is not None and price is not None:
        route = Route.query.filter(Route.id == id).first()
        if route is None:
            return Response(json.dumps({"message": "Error"}), status=200)
        if route.capacity - route.capacityLeft > capacity:
            return Response(json.dumps({"message": "Capacity minimum"}), status=200)
        
        route.name = name
        route.capacityLeft = route.capacityLeft + capacity - route.capacity
        route.capacity = capacity
        route.date = date
        route.summary = summary
        route.description = description
        route.gpx = gpx
        route.photo = photo
        route.price = price
        database.session.commit()

        peaksOfRoute = RoutePeak.query.filter(RoutePeak.routeId == route.id).all()
        for peak in peaksOfRoute:
            database.session.delete(peak)
            database.session.commit()

        for peak in peaks:
            peakFromDatabase = Peak.query.filter(Peak.name == peak['name']).first()
            if peakFromDatabase is not None:
                routePeakInDatabase = RoutePeak.query.filter(and_(RoutePeak.routeId == route.id, RoutePeak.peakId == peakFromDatabase.id)).first()
                if routePeakInDatabase is None:
                    routePeak = RoutePeak(routeId = route.id, peakId = peakFromDatabase.id)
                    database.session.add(routePeak)
                    database.session.commit()
            else:
                newPeak = Peak(name=peak['name'], elevation=peak['elevation'])
                database.session.add(newPeak)
                database.session.commit()
                routePeak = RoutePeak(routeId = route.id, peakId = newPeak.id)
                database.session.add(routePeak)
                database.session.commit()

        return Response(json.dumps({"message":"Ok"}), status=200)

    return Response(json.dumps({"message":"Error"}), status=200)


@application.route("/routes/getFutureRoutes", methods=["GET"])
def getFutureRoutes():
    current_time = datetime.utcnow()
    routes = Route.query.filter(
        Route.date > current_time
    ).all()
    routes = [
        {
            "id": route.id,
            "name": route.name,
            "capacity": route.capacity,
            "capacityLeft": route.capacityLeft,
            "date": route.date,
            "summary": route.summary,
            "description": route.description,
            "gpx": route.gpx,
            "photo":route.photo,
            "price":route.price,
            "peaks": [{
                "name": peak.name,
                "elevation": peak.elevation
            } for peak in route.peaks]
        }
        for route in routes
    ]
    return Response(json.dumps(routes), status=200)


@application.route("/routes/registerUserForRoute", methods=["POST"])
def registerUserForRoute():
    userId = request.json.get("userId", None)
    routeId = request.json.get("routeId", None)

    userNotExists = User.query.filter(User.id == userId).first() is None
    route = Route.query.filter(Route.id == routeId).first()
    routeNotExists = route is None

    if userNotExists or routeNotExists:
        return Response(json.dumps({'message':"Error"}), status=200)
    
    registeredAlready = UserRoute.query.filter(and_(UserRoute.userId == userId, UserRoute.routeId == routeId)).first() is not None
   
    if registeredAlready:
        return Response(json.dumps({'message':"Exists already"}), status=200)

    route.capacityLeft = route.capactityLeft - 1 

    userRoute = UserRoute(userId=userId, routeId=routeId)
    database.session.add(userRoute)
    database.session.commit()

    return Response(json.dumps({'message':"Ok"}), status=200)
############################################################################


if __name__ == "__main__":
    database.init_app(application)
    application.run(debug=True, host="0.0.0.0", port=5000)
