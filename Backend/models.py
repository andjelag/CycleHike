from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import MEDIUMTEXT

database = SQLAlchemy()


class UserRole(database.Model):
    __tablename__ = "userrole"
    id = database.Column(database.Integer, primary_key=True)
    userId = database.Column(
        database.Integer, database.ForeignKey("users.id"), nullable=False
    )
    roleId = database.Column(
        database.Integer, database.ForeignKey("roles.id"), nullable=False
    )

class UserRoute(database.Model):
    __tablename__ = "userroute"
    id = database.Column(database.Integer, primary_key=True)
    userId = database.Column(
        database.Integer, database.ForeignKey("users.id", ondelete='CASCADE'), nullable=False
    )
    routeId = database.Column(
        database.Integer, database.ForeignKey("routes.id", ondelete='CASCADE'), nullable=False
    )


class RoutePeak(database.Model):
    __tablename__ = "routepeak"
    id = database.Column(database.Integer, primary_key=True)
    routeId = database.Column(
        database.Integer, database.ForeignKey("routes.id"), nullable=False
    )
    peakId = database.Column(
        database.Integer, database.ForeignKey("peaks.id"), nullable=False
    )


class User(database.Model):
    __tablename__ = "users"
    id = database.Column(database.Integer, primary_key=True)
    forename = database.Column(database.String(256), nullable=False)
    surname = database.Column(database.String(256), nullable=False)
    email = database.Column(database.String(256), nullable=False, unique=True)
    password = database.Column(database.String(256), nullable=False)
    phone = database.Column(database.String(256), nullable=False)
    photo = database.Column(MEDIUMTEXT, nullable=False)
    status = database.Column(database.String(1), nullable=False)

    roles = database.relationship(
        "Role", secondary=UserRole.__table__, back_populates="users"
    )

    routes = database.relationship(
        "Route", secondary=UserRoute.__table__, back_populates="users"
    )

    def __repr__(self):
        return self.email


class Role(database.Model):
    __tablename__ = "roles"
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(256), nullable=False)

    users = database.relationship(
        "User", secondary=UserRole.__table__, back_populates="roles"
    )

    def __repr__(self):
        return self.name


class Route(database.Model):
    __tablename__ = "routes"
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(256), nullable=False)
    capacity = database.Column(database.Integer, nullable=False)
    capacityLeft = database.Column(database.Integer, nullable=False)
    date = database.Column(database.DateTime, nullable=False)
    summary = database.Column(database.String(1024), nullable=False)
    description = database.Column(database.Text(), nullable=False)
    gpx = database.Column(MEDIUMTEXT, nullable=True)
    photo = database.Column(MEDIUMTEXT, nullable=True)
    price = database.Column(database.Integer, nullable=False)

    users = database.relationship(
        "User", secondary=UserRoute.__table__, back_populates="routes"
    )

    peaks = database.relationship(
        "Peak", secondary=RoutePeak.__table__, back_populates="routes"
    )


class Peak(database.Model):
    __tablename__ = "peaks"
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(256), nullable=False, unique=True)
    elevation = database.Column(database.Integer, nullable=False)

    routes = database.relationship(
        "Route", secondary=RoutePeak.__table__, back_populates="peaks"
    )
