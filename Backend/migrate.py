from flask import Flask
from configuration import Configuration
from flask_migrate import Migrate, init, migrate, upgrade
from models import database, Role, UserRole, User, Route, UserRoute, Peak, RoutePeak
from sqlalchemy_utils import database_exists, create_database
import datetime

application = Flask(__name__)
application.config.from_object(Configuration)

migrateObject = Migrate(application, database)

if not database_exists(application.config["SQLALCHEMY_DATABASE_URI"]):
    create_database(application.config["SQLALCHEMY_DATABASE_URI"])

database.init_app(application)

with application.app_context() as context:
    init()
    migrate(message="Production migration")
    upgrade()

    roleForAdmin = Role(name="admin")
    roleForUser = Role(name="user")
    database.session.add(roleForAdmin)
    database.session.add(roleForUser)
    database.session.commit()

    admin = User(email="admin@gmail.com", password="aaa", forename="Admin", surname="", phone="", photo="../assets/user_icon.png", status="A")
    database.session.add(admin)
    database.session.commit()

    userRole = UserRole(userId=admin.id, roleId=roleForAdmin.id)
    database.session.add(userRole)
    database.session.commit()

    
    user = User(email="anaantic@gmail.com", password="Lozinka1.", forename="Ana", surname="Antic", phone="0607777777", photo="../assets/user_icon.png", status="A")
    database.session.add(user)
    database.session.commit()

    userRole = UserRole(userId=user.id, roleId=roleForUser.id)
    database.session.add(userRole)
    database.session.commit()

    route1 = Route(
        name="Kablar",
        capacity=40,
        capacityLeft=0,
        date=datetime.datetime(2023, 9, 30, 8, 0, 0),
        summary="Put do vrha stazom 3, kraj kod planinarskog doma",
        description="desc 1 ",
        gpx="""<?xml version="1.0" encoding="UTF-8"?>
<gpx creator="Wikiloc - https://www.wikiloc.com" version="1.1" xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">
  <metadata>
    <name>Kablar</name>
    <link href="https://www.wikiloc.com/hiking-trails/kablar-16006342">
      <text>Kablar</text>
    </link>
    <time>2017-01-02T13:38:06Z</time>
  </metadata>
  <trk>
    <name>Kablar</name>
    <cmt></cmt>
    <desc></desc>
    <trkseg>
      <trkpt lat="43.904630" lon="20.194447">
        <ele>284.389</ele>
        <time>2017-01-02T09:18:20Z</time>
      </trkpt>
      <trkpt lat="43.904806" lon="20.194387">
        <ele>288.406</ele>
        <time>2017-01-02T09:18:48Z</time>
      </trkpt>
      <trkpt lat="43.904881" lon="20.194568">
        <ele>287.326</ele>
        <time>2017-01-02T09:19:18Z</time>
      </trkpt>
      <trkpt lat="43.905061" lon="20.194318">
        <ele>293.708</ele>
        <time>2017-01-02T09:19:56Z</time>
      </trkpt>
      <trkpt lat="43.904580" lon="20.194052">
        <ele>288.649</ele>
        <time>2017-01-02T09:21:42Z</time>
      </trkpt>
      <trkpt lat="43.904137" lon="20.193029">
        <ele>306.694</ele>
        <time>2017-01-02T09:23:21Z</time>
      </trkpt>
      <trkpt lat="43.904145" lon="20.192085">
        <ele>322.328</ele>
        <time>2017-01-02T09:24:18Z</time>
      </trkpt>
      <trkpt lat="43.904341" lon="20.191811">
        <ele>332.188</ele>
        <time>2017-01-02T09:24:47Z</time>
      </trkpt>
      <trkpt lat="43.904505" lon="20.191874">
        <ele>340.634</ele>
        <time>2017-01-02T09:25:16Z</time>
      </trkpt>
      <trkpt lat="43.904726" lon="20.192433">
        <ele>346.931</ele>
        <time>2017-01-02T09:26:14Z</time>
      </trkpt>
      <trkpt lat="43.905003" lon="20.192632">
        <ele>353.822</ele>
        <time>2017-01-02T09:27:20Z</time>
      </trkpt>
      <trkpt lat="43.905182" lon="20.191910">
        <ele>372.710</ele>
        <time>2017-01-02T09:29:07Z</time>
      </trkpt>
      <trkpt lat="43.905395" lon="20.192184">
        <ele>382.992</ele>
        <time>2017-01-02T09:30:05Z</time>
      </trkpt>
      <trkpt lat="43.905850" lon="20.192180">
        <ele>403.873</ele>
        <time>2017-01-02T09:32:12Z</time>
      </trkpt>
      <trkpt lat="43.905964" lon="20.192388">
        <ele>399.420</ele>
        <time>2017-01-02T09:35:53Z</time>
      </trkpt>
      <trkpt lat="43.906104" lon="20.192353">
        <ele>405.608</ele>
        <time>2017-01-02T09:36:12Z</time>
      </trkpt>
      <trkpt lat="43.905880" lon="20.192145">
        <ele>406.190</ele>
        <time>2017-01-02T09:37:52Z</time>
      </trkpt>
      <trkpt lat="43.905974" lon="20.191657">
        <ele>427.715</ele>
        <time>2017-01-02T09:38:41Z</time>
      </trkpt>
      <trkpt lat="43.906179" lon="20.191944">
        <ele>429.419</ele>
        <time>2017-01-02T09:39:59Z</time>
      </trkpt>
      <trkpt lat="43.906578" lon="20.192119">
        <ele>439.559</ele>
        <time>2017-01-02T09:42:53Z</time>
      </trkpt>
      <trkpt lat="43.907184" lon="20.192021">
        <ele>477.895</ele>
        <time>2017-01-02T09:52:07Z</time>
      </trkpt>
      <trkpt lat="43.907390" lon="20.191841">
        <ele>498.322</ele>
        <time>2017-01-02T09:53:52Z</time>
      </trkpt>
      <trkpt lat="43.907373" lon="20.191932">
        <ele>494.213</ele>
        <time>2017-01-02T09:54:11Z</time>
      </trkpt>
      <trkpt lat="43.907535" lon="20.191652">
        <ele>513.061</ele>
        <time>2017-01-02T09:55:45Z</time>
      </trkpt>
      <trkpt lat="43.907439" lon="20.191925">
        <ele>498.678</ele>
        <time>2017-01-02T09:59:39Z</time>
      </trkpt>
      <trkpt lat="43.907586" lon="20.191642">
        <ele>519.733</ele>
        <time>2017-01-02T10:00:59Z</time>
      </trkpt>
      <trkpt lat="43.907715" lon="20.191880">
        <ele>516.526</ele>
        <time>2017-01-02T10:02:46Z</time>
      </trkpt>
      <trkpt lat="43.907798" lon="20.191811">
        <ele>529.108</ele>
        <time>2017-01-02T10:03:24Z</time>
      </trkpt>
      <trkpt lat="43.907688" lon="20.191806">
        <ele>520.278</ele>
        <time>2017-01-02T10:04:16Z</time>
      </trkpt>
      <trkpt lat="43.907742" lon="20.192263">
        <ele>503.083</ele>
        <time>2017-01-02T10:05:24Z</time>
      </trkpt>
      <trkpt lat="43.907999" lon="20.192464">
        <ele>521.677</ele>
        <time>2017-01-02T10:08:39Z</time>
      </trkpt>
      <trkpt lat="43.908228" lon="20.191949">
        <ele>555.697</ele>
        <time>2017-01-02T10:12:55Z</time>
      </trkpt>
      <trkpt lat="43.908807" lon="20.191555">
        <ele>595.553</ele>
        <time>2017-01-02T10:18:41Z</time>
      </trkpt>
      <trkpt lat="43.908858" lon="20.191379">
        <ele>604.760</ele>
        <time>2017-01-02T10:19:26Z</time>
      </trkpt>
      <trkpt lat="43.908536" lon="20.190325">
        <ele>616.691</ele>
        <time>2017-01-02T10:23:28Z</time>
      </trkpt>
      <trkpt lat="43.908348" lon="20.190274">
        <ele>594.649</ele>
        <time>2017-01-02T10:27:12Z</time>
      </trkpt>
      <trkpt lat="43.909100" lon="20.189755">
        <ele>671.377</ele>
        <time>2017-01-02T10:37:31Z</time>
      </trkpt>
      <trkpt lat="43.909498" lon="20.189915">
        <ele>697.361</ele>
        <time>2017-01-02T10:39:15Z</time>
      </trkpt>
      <trkpt lat="43.909783" lon="20.189807">
        <ele>709.527</ele>
        <time>2017-01-02T10:41:16Z</time>
      </trkpt>
      <trkpt lat="43.910083" lon="20.190156">
        <ele>720.708</ele>
        <time>2017-01-02T10:46:48Z</time>
      </trkpt>
      <trkpt lat="43.910397" lon="20.189996">
        <ele>743.178</ele>
        <time>2017-01-02T10:49:43Z</time>
      </trkpt>
      <trkpt lat="43.910667" lon="20.190165">
        <ele>762.213</ele>
        <time>2017-01-02T10:51:12Z</time>
      </trkpt>
      <trkpt lat="43.910837" lon="20.190114">
        <ele>772.777</ele>
        <time>2017-01-02T10:52:23Z</time>
      </trkpt>
      <trkpt lat="43.911192" lon="20.190508">
        <ele>797.217</ele>
        <time>2017-01-02T10:56:31Z</time>
      </trkpt>
      <trkpt lat="43.911742" lon="20.190483">
        <ele>827.163</ele>
        <time>2017-01-02T10:59:26Z</time>
      </trkpt>
      <trkpt lat="43.911838" lon="20.190859">
        <ele>832.870</ele>
        <time>2017-01-02T11:01:11Z</time>
      </trkpt>
      <trkpt lat="43.912109" lon="20.190746">
        <ele>847.481</ele>
        <time>2017-01-02T11:03:17Z</time>
      </trkpt>
      <trkpt lat="43.912532" lon="20.190951">
        <ele>863.879</ele>
        <time>2017-01-02T11:04:58Z</time>
      </trkpt>
      <trkpt lat="43.912568" lon="20.191385">
        <ele>861.011</ele>
        <time>2017-01-02T11:09:14Z</time>
      </trkpt>
      <trkpt lat="43.912447" lon="20.191203">
        <ele>858.621</ele>
        <time>2017-01-02T11:11:19Z</time>
      </trkpt>
      <trkpt lat="43.912602" lon="20.191594">
        <ele>861.103</ele>
        <time>2017-01-02T11:12:39Z</time>
      </trkpt>
      <trkpt lat="43.912495" lon="20.191918">
        <ele>859.808</ele>
        <time>2017-01-02T11:13:26Z</time>
      </trkpt>
      <trkpt lat="43.912257" lon="20.192096">
        <ele>852.622</ele>
        <time>2017-01-02T11:17:31Z</time>
      </trkpt>
      <trkpt lat="43.912392" lon="20.192158">
        <ele>857.147</ele>
        <time>2017-01-02T11:19:09Z</time>
      </trkpt>
      <trkpt lat="43.912257" lon="20.192860">
        <ele>839.481</ele>
        <time>2017-01-02T11:21:19Z</time>
      </trkpt>
      <trkpt lat="43.912153" lon="20.192484">
        <ele>844.711</ele>
        <time>2017-01-02T11:33:52Z</time>
      </trkpt>
      <trkpt lat="43.912319" lon="20.192770">
        <ele>843.357</ele>
        <time>2017-01-02T11:46:28Z</time>
      </trkpt>
      <trkpt lat="43.912729" lon="20.192855">
        <ele>847.324</ele>
        <time>2017-01-02T11:47:53Z</time>
      </trkpt>
      <trkpt lat="43.912734" lon="20.193104">
        <ele>840.545</ele>
        <time>2017-01-02T11:48:32Z</time>
      </trkpt>
      <trkpt lat="43.912169" lon="20.194007">
        <ele>813.233</ele>
        <time>2017-01-02T11:50:29Z</time>
      </trkpt>
      <trkpt lat="43.912073" lon="20.193941">
        <ele>812.412</ele>
        <time>2017-01-02T11:50:58Z</time>
      </trkpt>
      <trkpt lat="43.911778" lon="20.194375">
        <ele>811.332</ele>
        <time>2017-01-02T11:53:16Z</time>
      </trkpt>
      <trkpt lat="43.911751" lon="20.194214">
        <ele>808.905</ele>
        <time>2017-01-02T11:54:30Z</time>
      </trkpt>
      <trkpt lat="43.911096" lon="20.194719">
        <ele>783.608</ele>
        <time>2017-01-02T11:56:16Z</time>
      </trkpt>
      <trkpt lat="43.911294" lon="20.195753">
        <ele>767.672</ele>
        <time>2017-01-02T12:05:17Z</time>
      </trkpt>
      <trkpt lat="43.911060" lon="20.196644">
        <ele>733.327</ele>
        <time>2017-01-02T12:07:57Z</time>
      </trkpt>
      <trkpt lat="43.910661" lon="20.197388">
        <ele>697.111</ele>
        <time>2017-01-02T12:11:38Z</time>
      </trkpt>
      <trkpt lat="43.911279" lon="20.195780">
        <ele>766.481</ele>
        <time>2017-01-02T12:20:04Z</time>
      </trkpt>
      <trkpt lat="43.911197" lon="20.195469">
        <ele>772.517</ele>
        <time>2017-01-02T12:22:30Z</time>
      </trkpt>
      <trkpt lat="43.911142" lon="20.195356">
        <ele>773.414</ele>
        <time>2017-01-02T12:24:07Z</time>
      </trkpt>
      <trkpt lat="43.910911" lon="20.195450">
        <ele>762.755</ele>
        <time>2017-01-02T12:26:00Z</time>
      </trkpt>
      <trkpt lat="43.910605" lon="20.194892">
        <ele>758.373</ele>
        <time>2017-01-02T12:28:21Z</time>
      </trkpt>
      <trkpt lat="43.909959" lon="20.194875">
        <ele>715.849</ele>
        <time>2017-01-02T12:30:14Z</time>
      </trkpt>
      <trkpt lat="43.909609" lon="20.194709">
        <ele>686.702</ele>
        <time>2017-01-02T12:31:21Z</time>
      </trkpt>
      <trkpt lat="43.909160" lon="20.194777">
        <ele>654.622</ele>
        <time>2017-01-02T12:32:46Z</time>
      </trkpt>
      <trkpt lat="43.908987" lon="20.194961">
        <ele>624.108</ele>
        <time>2017-01-02T12:36:20Z</time>
      </trkpt>
      <trkpt lat="43.909260" lon="20.195479">
        <ele>646.085</ele>
        <time>2017-01-02T12:37:52Z</time>
      </trkpt>
      <trkpt lat="43.909330" lon="20.196637">
        <ele>615.160</ele>
        <time>2017-01-02T12:40:52Z</time>
      </trkpt>
      <trkpt lat="43.909032" lon="20.196606">
        <ele>583.234</ele>
        <time>2017-01-02T12:44:31Z</time>
      </trkpt>
      <trkpt lat="43.908910" lon="20.197201">
        <ele>583.344</ele>
        <time>2017-01-02T13:02:41Z</time>
      </trkpt>
      <trkpt lat="43.908521" lon="20.197381">
        <ele>550.570</ele>
        <time>2017-01-02T13:03:47Z</time>
      </trkpt>
      <trkpt lat="43.908586" lon="20.197242">
        <ele>557.597</ele>
        <time>2017-01-02T13:04:06Z</time>
      </trkpt>
      <trkpt lat="43.908390" lon="20.197163">
        <ele>540.948</ele>
        <time>2017-01-02T13:04:46Z</time>
      </trkpt>
      <trkpt lat="43.908337" lon="20.197282">
        <ele>536.586</ele>
        <time>2017-01-02T13:05:27Z</time>
      </trkpt>
      <trkpt lat="43.908241" lon="20.197114">
        <ele>529.984</ele>
        <time>2017-01-02T13:05:46Z</time>
      </trkpt>
      <trkpt lat="43.908550" lon="20.196420">
        <ele>537.507</ele>
        <time>2017-01-02T13:07:17Z</time>
      </trkpt>
      <trkpt lat="43.908824" lon="20.194758">
        <ele>606.817</ele>
        <time>2017-01-02T13:09:29Z</time>
      </trkpt>
      <trkpt lat="43.907930" lon="20.194682">
        <ele>482.708</ele>
        <time>2017-01-02T13:10:57Z</time>
      </trkpt>
      <trkpt lat="43.908060" lon="20.193920">
        <ele>503.779</ele>
        <time>2017-01-02T13:11:45Z</time>
      </trkpt>
      <trkpt lat="43.907775" lon="20.193545">
        <ele>469.834</ele>
        <time>2017-01-02T13:13:03Z</time>
      </trkpt>
      <trkpt lat="43.907905" lon="20.192790">
        <ele>504.628</ele>
        <time>2017-01-02T13:14:28Z</time>
      </trkpt>
      <trkpt lat="43.907691" lon="20.192816">
        <ele>485.568</ele>
        <time>2017-01-02T13:14:58Z</time>
      </trkpt>
      <trkpt lat="43.907737" lon="20.192227">
        <ele>503.374</ele>
        <time>2017-01-02T13:16:22Z</time>
      </trkpt>
      <trkpt lat="43.905370" lon="20.193623">
        <ele>321.681</ele>
        <time>2017-01-02T13:24:00Z</time>
      </trkpt>
      <trkpt lat="43.905956" lon="20.192273">
        <ele>403.922</ele>
        <time>2017-01-02T13:24:48Z</time>
      </trkpt>
      <trkpt lat="43.905857" lon="20.191724">
        <ele>417.360</ele>
        <time>2017-01-02T13:25:36Z</time>
      </trkpt>
      <trkpt lat="43.905970" lon="20.192355">
        <ele>400.919</ele>
        <time>2017-01-02T13:26:54Z</time>
      </trkpt>
      <trkpt lat="43.905641" lon="20.192278">
        <ele>392.109</ele>
        <time>2017-01-02T13:28:48Z</time>
      </trkpt>
      <trkpt lat="43.905433" lon="20.192434">
        <ele>379.719</ele>
        <time>2017-01-02T13:29:10Z</time>
      </trkpt>
      <trkpt lat="43.905460" lon="20.192247">
        <ele>385.008</ele>
        <time>2017-01-02T13:29:48Z</time>
      </trkpt>
      <trkpt lat="43.905235" lon="20.192232">
        <ele>374.522</ele>
        <time>2017-01-02T13:30:46Z</time>
      </trkpt>
      <trkpt lat="43.905150" lon="20.192620">
        <ele>361.547</ele>
        <time>2017-01-02T13:31:44Z</time>
      </trkpt>
      <trkpt lat="43.904895" lon="20.192693">
        <ele>348.071</ele>
        <time>2017-01-02T13:32:12Z</time>
      </trkpt>
      <trkpt lat="43.904362" lon="20.192140">
        <ele>332.691</ele>
        <time>2017-01-02T13:33:00Z</time>
      </trkpt>
      <trkpt lat="43.904208" lon="20.192323">
        <ele>323.217</ele>
        <time>2017-01-02T13:33:40Z</time>
      </trkpt>
      <trkpt lat="43.904426" lon="20.192831">
        <ele>325.414</ele>
        <time>2017-01-02T13:34:19Z</time>
      </trkpt>
      <trkpt lat="43.905033" lon="20.192941">
        <ele>346.615</ele>
        <time>2017-01-02T13:34:48Z</time>
      </trkpt>
      <trkpt lat="43.905033" lon="20.193502">
        <ele>322.433</ele>
        <time>2017-01-02T13:35:17Z</time>
      </trkpt>
      <trkpt lat="43.904750" lon="20.194228">
        <ele>289.757</ele>
        <time>2017-01-02T13:36:14Z</time>
      </trkpt>
      <trkpt lat="43.905135" lon="20.194138">
        <ele>298.100</ele>
        <time>2017-01-02T13:36:34Z</time>
      </trkpt>
      <trkpt lat="43.905168" lon="20.194319">
        <ele>294.520</ele>
        <time>2017-01-02T13:36:44Z</time>
      </trkpt>
      <trkpt lat="43.904941" lon="20.194766">
        <ele>285.408</ele>
        <time>2017-01-02T13:37:32Z</time>
      </trkpt>
      <trkpt lat="43.904626" lon="20.194446">
        <ele>284.346</ele>
        <time>2017-01-02T13:38:06Z</time>
      </trkpt>
    </trkseg>
  </trk></gpx>""",
        photo="../../assets/mountain_logo.webp",
        price=1200
    )

    database.session.add(route1)
    database.session.commit()

    route2 = Route(
        name="Kablar",
        capacity=50,
        capacityLeft=47,
        date=datetime.datetime(2023, 9, 30, 8, 0, 0),
        summary="Put do vrha stazom 2, kraj kod manastira ...",
        description="desc 2 ",
        gpx="""<?xml version="1.0" encoding="UTF-8"?>
<gpx creator="Wikiloc - https://www.wikiloc.com" version="1.1" xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">
  <metadata>
    <name>Kablar</name>
    <link href="https://www.wikiloc.com/hiking-trails/kablar-16006342">
      <text>Kablar</text>
    </link>
    <time>2017-01-02T13:38:06Z</time>
  </metadata>
  <trk>
    <name>Kablar</name>
    <cmt></cmt>
    <desc></desc>
    <trkseg>
      <trkpt lat="43.904630" lon="20.194447">
        <ele>284.389</ele>
        <time>2017-01-02T09:18:20Z</time>
      </trkpt>
      <trkpt lat="43.904806" lon="20.194387">
        <ele>288.406</ele>
        <time>2017-01-02T09:18:48Z</time>
      </trkpt>
      <trkpt lat="43.904881" lon="20.194568">
        <ele>287.326</ele>
        <time>2017-01-02T09:19:18Z</time>
      </trkpt>
      <trkpt lat="43.905061" lon="20.194318">
        <ele>293.708</ele>
        <time>2017-01-02T09:19:56Z</time>
      </trkpt>
      <trkpt lat="43.904580" lon="20.194052">
        <ele>288.649</ele>
        <time>2017-01-02T09:21:42Z</time>
      </trkpt>
      <trkpt lat="43.904137" lon="20.193029">
        <ele>306.694</ele>
        <time>2017-01-02T09:23:21Z</time>
      </trkpt>
      <trkpt lat="43.904145" lon="20.192085">
        <ele>322.328</ele>
        <time>2017-01-02T09:24:18Z</time>
      </trkpt>
      <trkpt lat="43.904341" lon="20.191811">
        <ele>332.188</ele>
        <time>2017-01-02T09:24:47Z</time>
      </trkpt>
      <trkpt lat="43.904505" lon="20.191874">
        <ele>340.634</ele>
        <time>2017-01-02T09:25:16Z</time>
      </trkpt>
      <trkpt lat="43.904726" lon="20.192433">
        <ele>346.931</ele>
        <time>2017-01-02T09:26:14Z</time>
      </trkpt>
      <trkpt lat="43.905003" lon="20.192632">
        <ele>353.822</ele>
        <time>2017-01-02T09:27:20Z</time>
      </trkpt>
      <trkpt lat="43.905182" lon="20.191910">
        <ele>372.710</ele>
        <time>2017-01-02T09:29:07Z</time>
      </trkpt>
      <trkpt lat="43.905395" lon="20.192184">
        <ele>382.992</ele>
        <time>2017-01-02T09:30:05Z</time>
      </trkpt>
      <trkpt lat="43.905850" lon="20.192180">
        <ele>403.873</ele>
        <time>2017-01-02T09:32:12Z</time>
      </trkpt>
      <trkpt lat="43.905964" lon="20.192388">
        <ele>399.420</ele>
        <time>2017-01-02T09:35:53Z</time>
      </trkpt>
      <trkpt lat="43.906104" lon="20.192353">
        <ele>405.608</ele>
        <time>2017-01-02T09:36:12Z</time>
      </trkpt>
      <trkpt lat="43.905880" lon="20.192145">
        <ele>406.190</ele>
        <time>2017-01-02T09:37:52Z</time>
      </trkpt>
      <trkpt lat="43.905974" lon="20.191657">
        <ele>427.715</ele>
        <time>2017-01-02T09:38:41Z</time>
      </trkpt>
      <trkpt lat="43.906179" lon="20.191944">
        <ele>429.419</ele>
        <time>2017-01-02T09:39:59Z</time>
      </trkpt>
      <trkpt lat="43.906578" lon="20.192119">
        <ele>439.559</ele>
        <time>2017-01-02T09:42:53Z</time>
      </trkpt>
      <trkpt lat="43.907184" lon="20.192021">
        <ele>477.895</ele>
        <time>2017-01-02T09:52:07Z</time>
      </trkpt>
      <trkpt lat="43.907390" lon="20.191841">
        <ele>498.322</ele>
        <time>2017-01-02T09:53:52Z</time>
      </trkpt>
      <trkpt lat="43.907373" lon="20.191932">
        <ele>494.213</ele>
        <time>2017-01-02T09:54:11Z</time>
      </trkpt>
      <trkpt lat="43.907535" lon="20.191652">
        <ele>513.061</ele>
        <time>2017-01-02T09:55:45Z</time>
      </trkpt>
      <trkpt lat="43.907439" lon="20.191925">
        <ele>498.678</ele>
        <time>2017-01-02T09:59:39Z</time>
      </trkpt>
      <trkpt lat="43.907586" lon="20.191642">
        <ele>519.733</ele>
        <time>2017-01-02T10:00:59Z</time>
      </trkpt>
      <trkpt lat="43.907715" lon="20.191880">
        <ele>516.526</ele>
        <time>2017-01-02T10:02:46Z</time>
      </trkpt>
      <trkpt lat="43.907798" lon="20.191811">
        <ele>529.108</ele>
        <time>2017-01-02T10:03:24Z</time>
      </trkpt>
      <trkpt lat="43.907688" lon="20.191806">
        <ele>520.278</ele>
        <time>2017-01-02T10:04:16Z</time>
      </trkpt>
      <trkpt lat="43.907742" lon="20.192263">
        <ele>503.083</ele>
        <time>2017-01-02T10:05:24Z</time>
      </trkpt>
      <trkpt lat="43.907999" lon="20.192464">
        <ele>521.677</ele>
        <time>2017-01-02T10:08:39Z</time>
      </trkpt>
      <trkpt lat="43.908228" lon="20.191949">
        <ele>555.697</ele>
        <time>2017-01-02T10:12:55Z</time>
      </trkpt>
      <trkpt lat="43.908807" lon="20.191555">
        <ele>595.553</ele>
        <time>2017-01-02T10:18:41Z</time>
      </trkpt>
      <trkpt lat="43.908858" lon="20.191379">
        <ele>604.760</ele>
        <time>2017-01-02T10:19:26Z</time>
      </trkpt>
      <trkpt lat="43.908536" lon="20.190325">
        <ele>616.691</ele>
        <time>2017-01-02T10:23:28Z</time>
      </trkpt>
      <trkpt lat="43.908348" lon="20.190274">
        <ele>594.649</ele>
        <time>2017-01-02T10:27:12Z</time>
      </trkpt>
      <trkpt lat="43.909100" lon="20.189755">
        <ele>671.377</ele>
        <time>2017-01-02T10:37:31Z</time>
      </trkpt>
      <trkpt lat="43.909498" lon="20.189915">
        <ele>697.361</ele>
        <time>2017-01-02T10:39:15Z</time>
      </trkpt>
      <trkpt lat="43.909783" lon="20.189807">
        <ele>709.527</ele>
        <time>2017-01-02T10:41:16Z</time>
      </trkpt>
      <trkpt lat="43.910083" lon="20.190156">
        <ele>720.708</ele>
        <time>2017-01-02T10:46:48Z</time>
      </trkpt>
      <trkpt lat="43.910397" lon="20.189996">
        <ele>743.178</ele>
        <time>2017-01-02T10:49:43Z</time>
      </trkpt>
      <trkpt lat="43.910667" lon="20.190165">
        <ele>762.213</ele>
        <time>2017-01-02T10:51:12Z</time>
      </trkpt>
      <trkpt lat="43.910837" lon="20.190114">
        <ele>772.777</ele>
        <time>2017-01-02T10:52:23Z</time>
      </trkpt>
      <trkpt lat="43.911192" lon="20.190508">
        <ele>797.217</ele>
        <time>2017-01-02T10:56:31Z</time>
      </trkpt>
      <trkpt lat="43.911742" lon="20.190483">
        <ele>827.163</ele>
        <time>2017-01-02T10:59:26Z</time>
      </trkpt>
      <trkpt lat="43.911838" lon="20.190859">
        <ele>832.870</ele>
        <time>2017-01-02T11:01:11Z</time>
      </trkpt>
      <trkpt lat="43.912109" lon="20.190746">
        <ele>847.481</ele>
        <time>2017-01-02T11:03:17Z</time>
      </trkpt>
      <trkpt lat="43.912532" lon="20.190951">
        <ele>863.879</ele>
        <time>2017-01-02T11:04:58Z</time>
      </trkpt>
      <trkpt lat="43.912568" lon="20.191385">
        <ele>861.011</ele>
        <time>2017-01-02T11:09:14Z</time>
      </trkpt>
      <trkpt lat="43.912447" lon="20.191203">
        <ele>858.621</ele>
        <time>2017-01-02T11:11:19Z</time>
      </trkpt>
      <trkpt lat="43.912602" lon="20.191594">
        <ele>861.103</ele>
        <time>2017-01-02T11:12:39Z</time>
      </trkpt>
      <trkpt lat="43.912495" lon="20.191918">
        <ele>859.808</ele>
        <time>2017-01-02T11:13:26Z</time>
      </trkpt>
      <trkpt lat="43.912257" lon="20.192096">
        <ele>852.622</ele>
        <time>2017-01-02T11:17:31Z</time>
      </trkpt>
      <trkpt lat="43.912392" lon="20.192158">
        <ele>857.147</ele>
        <time>2017-01-02T11:19:09Z</time>
      </trkpt>
      <trkpt lat="43.912257" lon="20.192860">
        <ele>839.481</ele>
        <time>2017-01-02T11:21:19Z</time>
      </trkpt>
      <trkpt lat="43.912153" lon="20.192484">
        <ele>844.711</ele>
        <time>2017-01-02T11:33:52Z</time>
      </trkpt>
      <trkpt lat="43.912319" lon="20.192770">
        <ele>843.357</ele>
        <time>2017-01-02T11:46:28Z</time>
      </trkpt>
      <trkpt lat="43.912729" lon="20.192855">
        <ele>847.324</ele>
        <time>2017-01-02T11:47:53Z</time>
      </trkpt>
      <trkpt lat="43.912734" lon="20.193104">
        <ele>840.545</ele>
        <time>2017-01-02T11:48:32Z</time>
      </trkpt>
      <trkpt lat="43.912169" lon="20.194007">
        <ele>813.233</ele>
        <time>2017-01-02T11:50:29Z</time>
      </trkpt>
      <trkpt lat="43.912073" lon="20.193941">
        <ele>812.412</ele>
        <time>2017-01-02T11:50:58Z</time>
      </trkpt>
      <trkpt lat="43.911778" lon="20.194375">
        <ele>811.332</ele>
        <time>2017-01-02T11:53:16Z</time>
      </trkpt>
      <trkpt lat="43.911751" lon="20.194214">
        <ele>808.905</ele>
        <time>2017-01-02T11:54:30Z</time>
      </trkpt>
      <trkpt lat="43.911096" lon="20.194719">
        <ele>783.608</ele>
        <time>2017-01-02T11:56:16Z</time>
      </trkpt>
      <trkpt lat="43.911294" lon="20.195753">
        <ele>767.672</ele>
        <time>2017-01-02T12:05:17Z</time>
      </trkpt>
      <trkpt lat="43.911060" lon="20.196644">
        <ele>733.327</ele>
        <time>2017-01-02T12:07:57Z</time>
      </trkpt>
      <trkpt lat="43.910661" lon="20.197388">
        <ele>697.111</ele>
        <time>2017-01-02T12:11:38Z</time>
      </trkpt>
      <trkpt lat="43.911279" lon="20.195780">
        <ele>766.481</ele>
        <time>2017-01-02T12:20:04Z</time>
      </trkpt>
      <trkpt lat="43.911197" lon="20.195469">
        <ele>772.517</ele>
        <time>2017-01-02T12:22:30Z</time>
      </trkpt>
      <trkpt lat="43.911142" lon="20.195356">
        <ele>773.414</ele>
        <time>2017-01-02T12:24:07Z</time>
      </trkpt>
      <trkpt lat="43.910911" lon="20.195450">
        <ele>762.755</ele>
        <time>2017-01-02T12:26:00Z</time>
      </trkpt>
      <trkpt lat="43.910605" lon="20.194892">
        <ele>758.373</ele>
        <time>2017-01-02T12:28:21Z</time>
      </trkpt>
      <trkpt lat="43.909959" lon="20.194875">
        <ele>715.849</ele>
        <time>2017-01-02T12:30:14Z</time>
      </trkpt>
      <trkpt lat="43.909609" lon="20.194709">
        <ele>686.702</ele>
        <time>2017-01-02T12:31:21Z</time>
      </trkpt>
      <trkpt lat="43.909160" lon="20.194777">
        <ele>654.622</ele>
        <time>2017-01-02T12:32:46Z</time>
      </trkpt>
      <trkpt lat="43.908987" lon="20.194961">
        <ele>624.108</ele>
        <time>2017-01-02T12:36:20Z</time>
      </trkpt>
      <trkpt lat="43.909260" lon="20.195479">
        <ele>646.085</ele>
        <time>2017-01-02T12:37:52Z</time>
      </trkpt>
      <trkpt lat="43.909330" lon="20.196637">
        <ele>615.160</ele>
        <time>2017-01-02T12:40:52Z</time>
      </trkpt>
      <trkpt lat="43.909032" lon="20.196606">
        <ele>583.234</ele>
        <time>2017-01-02T12:44:31Z</time>
      </trkpt>
      <trkpt lat="43.908910" lon="20.197201">
        <ele>583.344</ele>
        <time>2017-01-02T13:02:41Z</time>
      </trkpt>
      <trkpt lat="43.908521" lon="20.197381">
        <ele>550.570</ele>
        <time>2017-01-02T13:03:47Z</time>
      </trkpt>
      <trkpt lat="43.908586" lon="20.197242">
        <ele>557.597</ele>
        <time>2017-01-02T13:04:06Z</time>
      </trkpt>
      <trkpt lat="43.908390" lon="20.197163">
        <ele>540.948</ele>
        <time>2017-01-02T13:04:46Z</time>
      </trkpt>
      <trkpt lat="43.908337" lon="20.197282">
        <ele>536.586</ele>
        <time>2017-01-02T13:05:27Z</time>
      </trkpt>
      <trkpt lat="43.908241" lon="20.197114">
        <ele>529.984</ele>
        <time>2017-01-02T13:05:46Z</time>
      </trkpt>
      <trkpt lat="43.908550" lon="20.196420">
        <ele>537.507</ele>
        <time>2017-01-02T13:07:17Z</time>
      </trkpt>
      <trkpt lat="43.908824" lon="20.194758">
        <ele>606.817</ele>
        <time>2017-01-02T13:09:29Z</time>
      </trkpt>
      <trkpt lat="43.907930" lon="20.194682">
        <ele>482.708</ele>
        <time>2017-01-02T13:10:57Z</time>
      </trkpt>
      <trkpt lat="43.908060" lon="20.193920">
        <ele>503.779</ele>
        <time>2017-01-02T13:11:45Z</time>
      </trkpt>
      <trkpt lat="43.907775" lon="20.193545">
        <ele>469.834</ele>
        <time>2017-01-02T13:13:03Z</time>
      </trkpt>
      <trkpt lat="43.907905" lon="20.192790">
        <ele>504.628</ele>
        <time>2017-01-02T13:14:28Z</time>
      </trkpt>
      <trkpt lat="43.907691" lon="20.192816">
        <ele>485.568</ele>
        <time>2017-01-02T13:14:58Z</time>
      </trkpt>
      <trkpt lat="43.907737" lon="20.192227">
        <ele>503.374</ele>
        <time>2017-01-02T13:16:22Z</time>
      </trkpt>
      <trkpt lat="43.905370" lon="20.193623">
        <ele>321.681</ele>
        <time>2017-01-02T13:24:00Z</time>
      </trkpt>
      <trkpt lat="43.905956" lon="20.192273">
        <ele>403.922</ele>
        <time>2017-01-02T13:24:48Z</time>
      </trkpt>
      <trkpt lat="43.905857" lon="20.191724">
        <ele>417.360</ele>
        <time>2017-01-02T13:25:36Z</time>
      </trkpt>
      <trkpt lat="43.905970" lon="20.192355">
        <ele>400.919</ele>
        <time>2017-01-02T13:26:54Z</time>
      </trkpt>
      <trkpt lat="43.905641" lon="20.192278">
        <ele>392.109</ele>
        <time>2017-01-02T13:28:48Z</time>
      </trkpt>
      <trkpt lat="43.905433" lon="20.192434">
        <ele>379.719</ele>
        <time>2017-01-02T13:29:10Z</time>
      </trkpt>
      <trkpt lat="43.905460" lon="20.192247">
        <ele>385.008</ele>
        <time>2017-01-02T13:29:48Z</time>
      </trkpt>
      <trkpt lat="43.905235" lon="20.192232">
        <ele>374.522</ele>
        <time>2017-01-02T13:30:46Z</time>
      </trkpt>
      <trkpt lat="43.905150" lon="20.192620">
        <ele>361.547</ele>
        <time>2017-01-02T13:31:44Z</time>
      </trkpt>
      <trkpt lat="43.904895" lon="20.192693">
        <ele>348.071</ele>
        <time>2017-01-02T13:32:12Z</time>
      </trkpt>
      <trkpt lat="43.904362" lon="20.192140">
        <ele>332.691</ele>
        <time>2017-01-02T13:33:00Z</time>
      </trkpt>
      <trkpt lat="43.904208" lon="20.192323">
        <ele>323.217</ele>
        <time>2017-01-02T13:33:40Z</time>
      </trkpt>
      <trkpt lat="43.904426" lon="20.192831">
        <ele>325.414</ele>
        <time>2017-01-02T13:34:19Z</time>
      </trkpt>
      <trkpt lat="43.905033" lon="20.192941">
        <ele>346.615</ele>
        <time>2017-01-02T13:34:48Z</time>
      </trkpt>
      <trkpt lat="43.905033" lon="20.193502">
        <ele>322.433</ele>
        <time>2017-01-02T13:35:17Z</time>
      </trkpt>
      <trkpt lat="43.904750" lon="20.194228">
        <ele>289.757</ele>
        <time>2017-01-02T13:36:14Z</time>
      </trkpt>
      <trkpt lat="43.905135" lon="20.194138">
        <ele>298.100</ele>
        <time>2017-01-02T13:36:34Z</time>
      </trkpt>
      <trkpt lat="43.905168" lon="20.194319">
        <ele>294.520</ele>
        <time>2017-01-02T13:36:44Z</time>
      </trkpt>
      <trkpt lat="43.904941" lon="20.194766">
        <ele>285.408</ele>
        <time>2017-01-02T13:37:32Z</time>
      </trkpt>
      <trkpt lat="43.904626" lon="20.194446">
        <ele>284.346</ele>
        <time>2017-01-02T13:38:06Z</time>
      </trkpt>
    </trkseg>
  </trk></gpx>""",
        photo="../../assets/mountain_logo.webp",
        price=0
    )

    database.session.add(route2)
    database.session.commit()

    route3 = Route(
        name="Ovcar",
        capacity=45,
        capacityLeft=40,
        date=datetime.datetime(2023, 8, 30, 8, 0, 0),
        summary="Okupljanje u centru Ovcar Banje",
        description="desc 3",
        gpx="""<?xml version="1.0" encoding="UTF-8"?>
<gpx creator="Wikiloc - https://www.wikiloc.com" version="1.1" xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">
  <metadata>
    <name>Wikiloc - Ovčar - uspon sa istoka stazom 8A</name>
    <link href="https://www.wikiloc.com/hiking-trails/ovcar-uspon-sa-istoka-stazom-8a-111667069">
      <text>Ovčar - uspon sa istoka stazom 8A on Wikiloc</text>
    </link>
    <time>2021-07-28T13:48:37Z</time>
  </metadata>
  <trk>
    <name>Ovčar - uspon sa istoka stazom 8A</name>
    <cmt></cmt>
    <desc></desc>
    <trkseg>
      <trkpt lat="43.905233" lon="20.222985">
        <ele>392.871</ele>
        <time>2021-07-28T08:58:13Z</time>
      </trkpt>
      <trkpt lat="43.905343" lon="20.223540">
        <ele>400.841</ele>
        <time>2021-07-28T08:58:36Z</time>
      </trkpt>
      <trkpt lat="43.905162" lon="20.224477">
        <ele>415.515</ele>
        <time>2021-07-28T08:59:53Z</time>
      </trkpt>
      <trkpt lat="43.904747" lon="20.224915">
        <ele>425.509</ele>
        <time>2021-07-28T09:00:46Z</time>
      </trkpt>
      <trkpt lat="43.904622" lon="20.224453">
        <ele>427.458</ele>
        <time>2021-07-28T09:01:28Z</time>
      </trkpt>
      <trkpt lat="43.903748" lon="20.224018">
        <ele>432.688</ele>
        <time>2021-07-28T09:03:49Z</time>
      </trkpt>
      <trkpt lat="43.903873" lon="20.223823">
        <ele>433.818</ele>
        <time>2021-07-28T09:04:48Z</time>
      </trkpt>
      <trkpt lat="43.903875" lon="20.224092">
        <ele>436.853</ele>
        <time>2021-07-28T09:06:07Z</time>
      </trkpt>
      <trkpt lat="43.904350" lon="20.224747">
        <ele>431.593</ele>
        <time>2021-07-28T09:08:30Z</time>
      </trkpt>
      <trkpt lat="43.904212" lon="20.224580">
        <ele>429.284</ele>
        <time>2021-07-28T09:09:35Z</time>
      </trkpt>
      <trkpt lat="43.904132" lon="20.225067">
        <ele>446.067</ele>
        <time>2021-07-28T09:10:14Z</time>
      </trkpt>
      <trkpt lat="43.903483" lon="20.225723">
        <ele>455.123</ele>
        <time>2021-07-28T09:11:25Z</time>
      </trkpt>
      <trkpt lat="43.903808" lon="20.226005">
        <ele>458.226</ele>
        <time>2021-07-28T09:12:01Z</time>
      </trkpt>
      <trkpt lat="43.904658" lon="20.226338">
        <ele>465.214</ele>
        <time>2021-07-28T09:13:27Z</time>
      </trkpt>
      <trkpt lat="43.905118" lon="20.226957">
        <ele>470.154</ele>
        <time>2021-07-28T09:14:24Z</time>
      </trkpt>
      <trkpt lat="43.905758" lon="20.226812">
        <ele>475.109</ele>
        <time>2021-07-28T09:15:28Z</time>
      </trkpt>
      <trkpt lat="43.905847" lon="20.226942">
        <ele>476.409</ele>
        <time>2021-07-28T09:15:43Z</time>
      </trkpt>
      <trkpt lat="43.905290" lon="20.227608">
        <ele>482.082</ele>
        <time>2021-07-28T09:16:51Z</time>
      </trkpt>
      <trkpt lat="43.904383" lon="20.227833">
        <ele>489.172</ele>
        <time>2021-07-28T09:18:15Z</time>
      </trkpt>
      <trkpt lat="43.904677" lon="20.228073">
        <ele>492.112</ele>
        <time>2021-07-28T09:18:55Z</time>
      </trkpt>
      <trkpt lat="43.905213" lon="20.227973">
        <ele>495.567</ele>
        <time>2021-07-28T09:19:49Z</time>
      </trkpt>
      <trkpt lat="43.904660" lon="20.228357">
        <ele>501.457</ele>
        <time>2021-07-28T09:21:12Z</time>
      </trkpt>
      <trkpt lat="43.903990" lon="20.227747">
        <ele>507.128</ele>
        <time>2021-07-28T09:22:28Z</time>
      </trkpt>
      <trkpt lat="43.902685" lon="20.227255">
        <ele>516.971</ele>
        <time>2021-07-28T09:24:28Z</time>
      </trkpt>
      <trkpt lat="43.902953" lon="20.227408">
        <ele>520.737</ele>
        <time>2021-07-28T09:25:15Z</time>
      </trkpt>
      <trkpt lat="43.903492" lon="20.228122">
        <ele>536.140</ele>
        <time>2021-07-28T09:26:33Z</time>
      </trkpt>
      <trkpt lat="43.903712" lon="20.228782">
        <ele>540.466</ele>
        <time>2021-07-28T09:27:28Z</time>
      </trkpt>
      <trkpt lat="43.903440" lon="20.229468">
        <ele>543.929</ele>
        <time>2021-07-28T09:28:21Z</time>
      </trkpt>
      <trkpt lat="43.902848" lon="20.230172">
        <ele>546.921</ele>
        <time>2021-07-28T09:29:38Z</time>
      </trkpt>
      <trkpt lat="43.902690" lon="20.230187">
        <ele>547.609</ele>
        <time>2021-07-28T09:29:55Z</time>
      </trkpt>
      <trkpt lat="43.902637" lon="20.229910">
        <ele>548.837</ele>
        <time>2021-07-28T09:30:29Z</time>
      </trkpt>
      <trkpt lat="43.902103" lon="20.229422">
        <ele>551.317</ele>
        <time>2021-07-28T09:31:29Z</time>
      </trkpt>
      <trkpt lat="43.901035" lon="20.228988">
        <ele>556.567</ele>
        <time>2021-07-28T09:34:28Z</time>
      </trkpt>
      <trkpt lat="43.899783" lon="20.229948">
        <ele>562.252</ele>
        <time>2021-07-28T09:36:58Z</time>
      </trkpt>
      <trkpt lat="43.899515" lon="20.229882">
        <ele>563.312</ele>
        <time>2021-07-28T09:37:29Z</time>
      </trkpt>
      <trkpt lat="43.899875" lon="20.228743">
        <ele>574.263</ele>
        <time>2021-07-28T09:39:27Z</time>
      </trkpt>
      <trkpt lat="43.899813" lon="20.227393">
        <ele>586.226</ele>
        <time>2021-07-28T09:41:47Z</time>
      </trkpt>
      <trkpt lat="43.899657" lon="20.226970">
        <ele>589.442</ele>
        <time>2021-07-28T09:42:31Z</time>
      </trkpt>
      <trkpt lat="43.899165" lon="20.226625">
        <ele>590.785</ele>
        <time>2021-07-28T09:43:48Z</time>
      </trkpt>
      <trkpt lat="43.898880" lon="20.225747">
        <ele>597.045</ele>
        <time>2021-07-28T09:45:22Z</time>
      </trkpt>
      <trkpt lat="43.898262" lon="20.225737">
        <ele>603.447</ele>
        <time>2021-07-28T09:46:47Z</time>
      </trkpt>
      <trkpt lat="43.897998" lon="20.226012">
        <ele>606.211</ele>
        <time>2021-07-28T09:47:18Z</time>
      </trkpt>
      <trkpt lat="43.897373" lon="20.225898">
        <ele>612.309</ele>
        <time>2021-07-28T09:48:53Z</time>
      </trkpt>
      <trkpt lat="43.896812" lon="20.226762">
        <ele>620.265</ele>
        <time>2021-07-28T09:50:30Z</time>
      </trkpt>
      <trkpt lat="43.896730" lon="20.226587">
        <ele>622.325</ele>
        <time>2021-07-28T09:51:02Z</time>
      </trkpt>
      <trkpt lat="43.896667" lon="20.226693">
        <ele>626.045</ele>
        <time>2021-07-28T09:52:23Z</time>
      </trkpt>
      <trkpt lat="43.896695" lon="20.226527">
        <ele>628.610</ele>
        <time>2021-07-28T09:53:44Z</time>
      </trkpt>
      <trkpt lat="43.896617" lon="20.226682">
        <ele>630.960</ele>
        <time>2021-07-28T09:54:28Z</time>
      </trkpt>
      <trkpt lat="43.896725" lon="20.226490">
        <ele>632.921</ele>
        <time>2021-07-28T09:55:09Z</time>
      </trkpt>
      <trkpt lat="43.896790" lon="20.226710">
        <ele>636.364</ele>
        <time>2021-07-28T09:56:22Z</time>
      </trkpt>
      <trkpt lat="43.896703" lon="20.226613">
        <ele>641.260</ele>
        <time>2021-07-28T09:58:13Z</time>
      </trkpt>
      <trkpt lat="43.896655" lon="20.226923">
        <ele>643.573</ele>
        <time>2021-07-28T09:58:54Z</time>
      </trkpt>
      <trkpt lat="43.896467" lon="20.227060">
        <ele>645.388</ele>
        <time>2021-07-28T09:59:13Z</time>
      </trkpt>
      <trkpt lat="43.895805" lon="20.227122">
        <ele>650.924</ele>
        <time>2021-07-28T10:00:11Z</time>
      </trkpt>
      <trkpt lat="43.895520" lon="20.226993">
        <ele>653.526</ele>
        <time>2021-07-28T10:00:46Z</time>
      </trkpt>
      <trkpt lat="43.894922" lon="20.227178">
        <ele>658.609</ele>
        <time>2021-07-28T10:01:38Z</time>
      </trkpt>
      <trkpt lat="43.894893" lon="20.226920">
        <ele>661.359</ele>
        <time>2021-07-28T10:03:07Z</time>
      </trkpt>
      <trkpt lat="43.895073" lon="20.226682">
        <ele>669.959</ele>
        <time>2021-07-28T10:05:38Z</time>
      </trkpt>
      <trkpt lat="43.895027" lon="20.226302">
        <ele>680.369</ele>
        <time>2021-07-28T10:08:40Z</time>
      </trkpt>
      <trkpt lat="43.895635" lon="20.224570">
        <ele>712.614</ele>
        <time>2021-07-28T10:22:43Z</time>
      </trkpt>
      <trkpt lat="43.895563" lon="20.224348">
        <ele>715.884</ele>
        <time>2021-07-28T10:23:36Z</time>
      </trkpt>
      <trkpt lat="43.895688" lon="20.224362">
        <ele>720.935</ele>
        <time>2021-07-28T10:25:22Z</time>
      </trkpt>
      <trkpt lat="43.895627" lon="20.224573">
        <ele>726.498</ele>
        <time>2021-07-28T10:27:51Z</time>
      </trkpt>
      <trkpt lat="43.895990" lon="20.223778">
        <ele>760.164</ele>
        <time>2021-07-28T10:40:30Z</time>
      </trkpt>
      <trkpt lat="43.896355" lon="20.223518">
        <ele>766.317</ele>
        <time>2021-07-28T10:41:33Z</time>
      </trkpt>
      <trkpt lat="43.896498" lon="20.223610">
        <ele>771.656</ele>
        <time>2021-07-28T10:43:07Z</time>
      </trkpt>
      <trkpt lat="43.896395" lon="20.223458">
        <ele>777.559</ele>
        <time>2021-07-28T10:44:59Z</time>
      </trkpt>
      <trkpt lat="43.896398" lon="20.223578">
        <ele>779.014</ele>
        <time>2021-07-28T10:45:25Z</time>
      </trkpt>
      <trkpt lat="43.896237" lon="20.223563">
        <ele>783.209</ele>
        <time>2021-07-28T10:46:37Z</time>
      </trkpt>
      <trkpt lat="43.896083" lon="20.223270">
        <ele>804.176</ele>
        <time>2021-07-28T10:48:28Z</time>
      </trkpt>
      <trkpt lat="43.896578" lon="20.220995">
        <ele>856.516</ele>
        <time>2021-07-28T10:56:21Z</time>
      </trkpt>
      <trkpt lat="43.896597" lon="20.220602">
        <ele>862.846</ele>
        <time>2021-07-28T10:57:14Z</time>
      </trkpt>
      <trkpt lat="43.896345" lon="20.219738">
        <ele>877.891</ele>
        <time>2021-07-28T10:59:15Z</time>
      </trkpt>
      <trkpt lat="43.896447" lon="20.219487">
        <ele>883.121</ele>
        <time>2021-07-28T10:59:55Z</time>
      </trkpt>
      <trkpt lat="43.896398" lon="20.218622">
        <ele>907.292</ele>
        <time>2021-07-28T11:05:38Z</time>
      </trkpt>
      <trkpt lat="43.896480" lon="20.218747">
        <ele>910.425</ele>
        <time>2021-07-28T11:06:38Z</time>
      </trkpt>
      <trkpt lat="43.896360" lon="20.218358">
        <ele>929.851</ele>
        <time>2021-07-28T11:13:43Z</time>
      </trkpt>
      <trkpt lat="43.896487" lon="20.217980">
        <ele>938.554</ele>
        <time>2021-07-28T11:15:09Z</time>
      </trkpt>
      <trkpt lat="43.896575" lon="20.218040">
        <ele>940.951</ele>
        <time>2021-07-28T11:15:44Z</time>
      </trkpt>
      <trkpt lat="43.896472" lon="20.217458">
        <ele>953.101</ele>
        <time>2021-07-28T11:18:05Z</time>
      </trkpt>
      <trkpt lat="43.896112" lon="20.217073">
        <ele>957.811</ele>
        <time>2021-07-28T11:20:47Z</time>
      </trkpt>
      <trkpt lat="43.896075" lon="20.216762">
        <ele>958.709</ele>
        <time>2021-07-28T11:21:09Z</time>
      </trkpt>
      <trkpt lat="43.896280" lon="20.215263">
        <ele>960.926</ele>
        <time>2021-07-28T11:23:15Z</time>
      </trkpt>
      <trkpt lat="43.896418" lon="20.215327">
        <ele>960.786</ele>
        <time>2021-07-28T11:23:43Z</time>
      </trkpt>
      <trkpt lat="43.896452" lon="20.215072">
        <ele>957.556</ele>
        <time>2021-07-28T11:27:17Z</time>
      </trkpt>
      <trkpt lat="43.896720" lon="20.214855">
        <ele>956.491</ele>
        <time>2021-07-28T11:27:57Z</time>
      </trkpt>
      <trkpt lat="43.896890" lon="20.215558">
        <ele>956.461</ele>
        <time>2021-07-28T11:29:04Z</time>
      </trkpt>
      <trkpt lat="43.896713" lon="20.215585">
        <ele>956.642</ele>
        <time>2021-07-28T11:30:45Z</time>
      </trkpt>
      <trkpt lat="43.896760" lon="20.215485">
        <ele>956.835</ele>
        <time>2021-07-28T11:33:01Z</time>
      </trkpt>
      <trkpt lat="43.896778" lon="20.215613">
        <ele>957.821</ele>
        <time>2021-07-28T11:45:07Z</time>
      </trkpt>
      <trkpt lat="43.896918" lon="20.215562">
        <ele>958.174</ele>
        <time>2021-07-28T11:47:37Z</time>
      </trkpt>
      <trkpt lat="43.896790" lon="20.215587">
        <ele>958.345</ele>
        <time>2021-07-28T11:49:54Z</time>
      </trkpt>
      <trkpt lat="43.896818" lon="20.215487">
        <ele>958.447</ele>
        <time>2021-07-28T11:50:34Z</time>
      </trkpt>
      <trkpt lat="43.896772" lon="20.215613">
        <ele>958.711</ele>
        <time>2021-07-28T11:54:25Z</time>
      </trkpt>
      <trkpt lat="43.896718" lon="20.215410">
        <ele>957.509</ele>
        <time>2021-07-28T11:55:04Z</time>
      </trkpt>
      <trkpt lat="43.896733" lon="20.214517">
        <ele>959.475</ele>
        <time>2021-07-28T11:56:30Z</time>
      </trkpt>
      <trkpt lat="43.896320" lon="20.213828">
        <ele>959.075</ele>
        <time>2021-07-28T11:57:34Z</time>
      </trkpt>
      <trkpt lat="43.896410" lon="20.213365">
        <ele>959.335</ele>
        <time>2021-07-28T11:58:18Z</time>
      </trkpt>
      <trkpt lat="43.896395" lon="20.213498">
        <ele>959.670</ele>
        <time>2021-07-28T12:00:29Z</time>
      </trkpt>
      <trkpt lat="43.896872" lon="20.213815">
        <ele>960.190</ele>
        <time>2021-07-28T12:01:21Z</time>
      </trkpt>
      <trkpt lat="43.896925" lon="20.213993">
        <ele>960.371</ele>
        <time>2021-07-28T12:01:46Z</time>
      </trkpt>
      <trkpt lat="43.896765" lon="20.214947">
        <ele>956.944</ele>
        <time>2021-07-28T12:03:00Z</time>
      </trkpt>
      <trkpt lat="43.896370" lon="20.215247">
        <ele>960.740</ele>
        <time>2021-07-28T12:03:51Z</time>
      </trkpt>
      <trkpt lat="43.896127" lon="20.214823">
        <ele>955.943</ele>
        <time>2021-07-28T12:04:35Z</time>
      </trkpt>
      <trkpt lat="43.896013" lon="20.215207">
        <ele>949.065</ele>
        <time>2021-07-28T12:05:18Z</time>
      </trkpt>
      <trkpt lat="43.895863" lon="20.214963">
        <ele>944.568</ele>
        <time>2021-07-28T12:05:43Z</time>
      </trkpt>
      <trkpt lat="43.895533" lon="20.214898">
        <ele>937.214</ele>
        <time>2021-07-28T12:06:16Z</time>
      </trkpt>
      <trkpt lat="43.895178" lon="20.214577">
        <ele>932.409</ele>
        <time>2021-07-28T12:06:56Z</time>
      </trkpt>
      <trkpt lat="43.894773" lon="20.213638">
        <ele>923.557</ele>
        <time>2021-07-28T12:08:04Z</time>
      </trkpt>
      <trkpt lat="43.894683" lon="20.214447">
        <ele>913.777</ele>
        <time>2021-07-28T12:09:06Z</time>
      </trkpt>
      <trkpt lat="43.894872" lon="20.214817">
        <ele>909.597</ele>
        <time>2021-07-28T12:09:37Z</time>
      </trkpt>
      <trkpt lat="43.894417" lon="20.214917">
        <ele>901.632</ele>
        <time>2021-07-28T12:10:24Z</time>
      </trkpt>
      <trkpt lat="43.894218" lon="20.214683">
        <ele>897.012</ele>
        <time>2021-07-28T12:10:51Z</time>
      </trkpt>
      <trkpt lat="43.894078" lon="20.213223">
        <ele>880.063</ele>
        <time>2021-07-28T12:12:34Z</time>
      </trkpt>
      <trkpt lat="43.894273" lon="20.212687">
        <ele>872.936</ele>
        <time>2021-07-28T12:13:20Z</time>
      </trkpt>
      <trkpt lat="43.894080" lon="20.212693">
        <ele>869.192</ele>
        <time>2021-07-28T12:13:43Z</time>
      </trkpt>
      <trkpt lat="43.893725" lon="20.213187">
        <ele>859.625</ele>
        <time>2021-07-28T12:14:42Z</time>
      </trkpt>
      <trkpt lat="43.893605" lon="20.213152">
        <ele>857.152</ele>
        <time>2021-07-28T12:14:54Z</time>
      </trkpt>
      <trkpt lat="43.893533" lon="20.212703">
        <ele>850.853</ele>
        <time>2021-07-28T12:15:29Z</time>
      </trkpt>
      <trkpt lat="43.893713" lon="20.212040">
        <ele>842.008</ele>
        <time>2021-07-28T12:16:19Z</time>
      </trkpt>
      <trkpt lat="43.893155" lon="20.212428">
        <ele>832.809</ele>
        <time>2021-07-28T12:17:18Z</time>
      </trkpt>
      <trkpt lat="43.892897" lon="20.211652">
        <ele>820.716</ele>
        <time>2021-07-28T12:18:21Z</time>
      </trkpt>
      <trkpt lat="43.891702" lon="20.211297">
        <ele>805.676</ele>
        <time>2021-07-28T12:20:32Z</time>
      </trkpt>
      <trkpt lat="43.891190" lon="20.210610">
        <ele>796.656</ele>
        <time>2021-07-28T12:22:14Z</time>
      </trkpt>
      <trkpt lat="43.891152" lon="20.210325">
        <ele>793.921</ele>
        <time>2021-07-28T12:22:44Z</time>
      </trkpt>
      <trkpt lat="43.890212" lon="20.210657">
        <ele>785.241</ele>
        <time>2021-07-28T12:24:20Z</time>
      </trkpt>
      <trkpt lat="43.890610" lon="20.210820">
        <ele>779.262</ele>
        <time>2021-07-28T12:25:08Z</time>
      </trkpt>
      <trkpt lat="43.890905" lon="20.211188">
        <ele>774.155</ele>
        <time>2021-07-28T12:25:44Z</time>
      </trkpt>
      <trkpt lat="43.890853" lon="20.211317">
        <ele>773.181</ele>
        <time>2021-07-28T12:25:52Z</time>
      </trkpt>
      <trkpt lat="43.890550" lon="20.211228">
        <ele>770.144</ele>
        <time>2021-07-28T12:26:21Z</time>
      </trkpt>
      <trkpt lat="43.889693" lon="20.211838">
        <ele>756.359</ele>
        <time>2021-07-28T12:28:11Z</time>
      </trkpt>
      <trkpt lat="43.890172" lon="20.211798">
        <ele>745.403</ele>
        <time>2021-07-28T12:29:13Z</time>
      </trkpt>
      <trkpt lat="43.890432" lon="20.212205">
        <ele>739.523</ele>
        <time>2021-07-28T12:29:53Z</time>
      </trkpt>
      <trkpt lat="43.890245" lon="20.213977">
        <ele>722.609</ele>
        <time>2021-07-28T12:32:19Z</time>
      </trkpt>
      <trkpt lat="43.890295" lon="20.214417">
        <ele>718.766</ele>
        <time>2021-07-28T12:32:49Z</time>
      </trkpt>
      <trkpt lat="43.890570" lon="20.214665">
        <ele>714.076</ele>
        <time>2021-07-28T12:33:30Z</time>
      </trkpt>
      <trkpt lat="43.890582" lon="20.214893">
        <ele>711.696</ele>
        <time>2021-07-28T12:33:44Z</time>
      </trkpt>
      <trkpt lat="43.890405" lon="20.214993">
        <ele>708.871</ele>
        <time>2021-07-28T12:34:04Z</time>
      </trkpt>
      <trkpt lat="43.889975" lon="20.214900">
        <ele>702.581</ele>
        <time>2021-07-28T12:34:44Z</time>
      </trkpt>
      <trkpt lat="43.889673" lon="20.214438">
        <ele>696.442</ele>
        <time>2021-07-28T12:35:24Z</time>
      </trkpt>
      <trkpt lat="43.889578" lon="20.213962">
        <ele>691.895</ele>
        <time>2021-07-28T12:36:02Z</time>
      </trkpt>
      <trkpt lat="43.889448" lon="20.214522">
        <ele>686.521</ele>
        <time>2021-07-28T12:36:41Z</time>
      </trkpt>
      <trkpt lat="43.889497" lon="20.215742">
        <ele>673.034</ele>
        <time>2021-07-28T12:38:04Z</time>
      </trkpt>
      <trkpt lat="43.888922" lon="20.216610">
        <ele>659.628</ele>
        <time>2021-07-28T12:39:30Z</time>
      </trkpt>
      <trkpt lat="43.888785" lon="20.218193">
        <ele>657.189</ele>
        <time>2021-07-28T12:41:01Z</time>
      </trkpt>
      <trkpt lat="43.889265" lon="20.220235">
        <ele>653.917</ele>
        <time>2021-07-28T12:43:02Z</time>
      </trkpt>
      <trkpt lat="43.889652" lon="20.220958">
        <ele>646.009</ele>
        <time>2021-07-28T12:43:49Z</time>
      </trkpt>
      <trkpt lat="43.889690" lon="20.222687">
        <ele>636.523</ele>
        <time>2021-07-28T12:45:23Z</time>
      </trkpt>
      <trkpt lat="43.889858" lon="20.223413">
        <ele>636.733</ele>
        <time>2021-07-28T12:46:24Z</time>
      </trkpt>
      <trkpt lat="43.890128" lon="20.223970">
        <ele>635.913</ele>
        <time>2021-07-28T12:47:00Z</time>
      </trkpt>
      <trkpt lat="43.890468" lon="20.224212">
        <ele>631.688</ele>
        <time>2021-07-28T12:47:30Z</time>
      </trkpt>
      <trkpt lat="43.890538" lon="20.224092">
        <ele>631.028</ele>
        <time>2021-07-28T12:48:36Z</time>
      </trkpt>
      <trkpt lat="43.890797" lon="20.224373">
        <ele>630.329</ele>
        <time>2021-07-28T12:49:35Z</time>
      </trkpt>
      <trkpt lat="43.891168" lon="20.225190">
        <ele>629.272</ele>
        <time>2021-07-28T12:50:32Z</time>
      </trkpt>
      <trkpt lat="43.891093" lon="20.225812">
        <ele>628.278</ele>
        <time>2021-07-28T12:51:34Z</time>
      </trkpt>
      <trkpt lat="43.891225" lon="20.226560">
        <ele>625.281</ele>
        <time>2021-07-28T12:52:19Z</time>
      </trkpt>
      <trkpt lat="43.891467" lon="20.227025">
        <ele>621.866</ele>
        <time>2021-07-28T12:52:55Z</time>
      </trkpt>
      <trkpt lat="43.891518" lon="20.227785">
        <ele>615.929</ele>
        <time>2021-07-28T12:54:29Z</time>
      </trkpt>
      <trkpt lat="43.891850" lon="20.228247">
        <ele>612.021</ele>
        <time>2021-07-28T12:55:22Z</time>
      </trkpt>
      <trkpt lat="43.892670" lon="20.228673">
        <ele>604.909</ele>
        <time>2021-07-28T12:56:51Z</time>
      </trkpt>
      <trkpt lat="43.893042" lon="20.228430">
        <ele>601.437</ele>
        <time>2021-07-28T12:57:40Z</time>
      </trkpt>
      <trkpt lat="43.893653" lon="20.228503">
        <ele>596.487</ele>
        <time>2021-07-28T12:58:31Z</time>
      </trkpt>
      <trkpt lat="43.893795" lon="20.228690">
        <ele>594.987</ele>
        <time>2021-07-28T12:58:50Z</time>
      </trkpt>
      <trkpt lat="43.894052" lon="20.228628">
        <ele>592.662</ele>
        <time>2021-07-28T12:59:15Z</time>
      </trkpt>
      <trkpt lat="43.894597" lon="20.229075">
        <ele>589.012</ele>
        <time>2021-07-28T13:00:14Z</time>
      </trkpt>
      <trkpt lat="43.895005" lon="20.229212">
        <ele>587.443</ele>
        <time>2021-07-28T13:00:50Z</time>
      </trkpt>
      <trkpt lat="43.895812" lon="20.228628">
        <ele>583.956</ele>
        <time>2021-07-28T13:02:10Z</time>
      </trkpt>
      <trkpt lat="43.896350" lon="20.228585">
        <ele>581.892</ele>
        <time>2021-07-28T13:03:03Z</time>
      </trkpt>
      <trkpt lat="43.896793" lon="20.228862">
        <ele>580.085</ele>
        <time>2021-07-28T13:03:47Z</time>
      </trkpt>
      <trkpt lat="43.897118" lon="20.228237">
        <ele>577.848</ele>
        <time>2021-07-28T13:04:41Z</time>
      </trkpt>
      <trkpt lat="43.897715" lon="20.227917">
        <ele>575.461</ele>
        <time>2021-07-28T13:05:35Z</time>
      </trkpt>
      <trkpt lat="43.897933" lon="20.227517">
        <ele>573.917</ele>
        <time>2021-07-28T13:06:07Z</time>
      </trkpt>
      <trkpt lat="43.898245" lon="20.227708">
        <ele>572.109</ele>
        <time>2021-07-28T13:06:38Z</time>
      </trkpt>
      <trkpt lat="43.898455" lon="20.228127">
        <ele>570.765</ele>
        <time>2021-07-28T13:07:09Z</time>
      </trkpt>
      <trkpt lat="43.898953" lon="20.228585">
        <ele>568.445</ele>
        <time>2021-07-28T13:07:59Z</time>
      </trkpt>
      <trkpt lat="43.899447" lon="20.229865">
        <ele>564.185</ele>
        <time>2021-07-28T13:09:40Z</time>
      </trkpt>
      <trkpt lat="43.899692" lon="20.229868">
        <ele>563.290</ele>
        <time>2021-07-28T13:09:59Z</time>
      </trkpt>
      <trkpt lat="43.901022" lon="20.228940">
        <ele>556.610</ele>
        <time>2021-07-28T13:12:30Z</time>
      </trkpt>
      <trkpt lat="43.902168" lon="20.229358">
        <ele>551.351</ele>
        <time>2021-07-28T13:14:33Z</time>
      </trkpt>
      <trkpt lat="43.902752" lon="20.230132">
        <ele>547.554</ele>
        <time>2021-07-28T13:15:59Z</time>
      </trkpt>
      <trkpt lat="43.903727" lon="20.228857">
        <ele>540.570</ele>
        <time>2021-07-28T13:18:20Z</time>
      </trkpt>
      <trkpt lat="43.903510" lon="20.228290">
        <ele>536.763</ele>
        <time>2021-07-28T13:18:57Z</time>
      </trkpt>
      <trkpt lat="43.902243" lon="20.226688">
        <ele>522.419</ele>
        <time>2021-07-28T13:21:36Z</time>
      </trkpt>
      <trkpt lat="43.902772" lon="20.227083">
        <ele>517.409</ele>
        <time>2021-07-28T13:22:40Z</time>
      </trkpt>
      <trkpt lat="43.903958" lon="20.227593">
        <ele>507.419</ele>
        <time>2021-07-28T13:24:32Z</time>
      </trkpt>
      <trkpt lat="43.904690" lon="20.228255">
        <ele>500.309</ele>
        <time>2021-07-28T13:25:44Z</time>
      </trkpt>
      <trkpt lat="43.905187" lon="20.227955">
        <ele>495.552</ele>
        <time>2021-07-28T13:26:47Z</time>
      </trkpt>
      <trkpt lat="43.904750" lon="20.228082">
        <ele>492.932</ele>
        <time>2021-07-28T13:27:27Z</time>
      </trkpt>
      <trkpt lat="43.904295" lon="20.227788">
        <ele>489.072</ele>
        <time>2021-07-28T13:28:22Z</time>
      </trkpt>
      <trkpt lat="43.905407" lon="20.227502">
        <ele>481.267</ele>
        <time>2021-07-28T13:29:58Z</time>
      </trkpt>
      <trkpt lat="43.905838" lon="20.226992">
        <ele>477.417</ele>
        <time>2021-07-28T13:30:43Z</time>
      </trkpt>
      <trkpt lat="43.905832" lon="20.226803">
        <ele>476.258</ele>
        <time>2021-07-28T13:30:58Z</time>
      </trkpt>
      <trkpt lat="43.904945" lon="20.226872">
        <ele>470.031</ele>
        <time>2021-07-28T13:32:11Z</time>
      </trkpt>
      <trkpt lat="43.904645" lon="20.226305">
        <ele>466.367</ele>
        <time>2021-07-28T13:33:02Z</time>
      </trkpt>
      <trkpt lat="43.903833" lon="20.226117">
        <ele>459.590</ele>
        <time>2021-07-28T13:34:57Z</time>
      </trkpt>
      <trkpt lat="43.903365" lon="20.225675">
        <ele>455.418</ele>
        <time>2021-07-28T13:35:37Z</time>
      </trkpt>
      <trkpt lat="43.904055" lon="20.225053">
        <ele>447.998</ele>
        <time>2021-07-28T13:36:40Z</time>
      </trkpt>
      <trkpt lat="43.904240" lon="20.224600">
        <ele>430.917</ele>
        <time>2021-07-28T13:37:17Z</time>
      </trkpt>
      <trkpt lat="43.903785" lon="20.223960">
        <ele>441.409</ele>
        <time>2021-07-28T13:38:30Z</time>
      </trkpt>
      <trkpt lat="43.903585" lon="20.223992">
        <ele>449.842</ele>
        <time>2021-07-28T13:39:24Z</time>
      </trkpt>
      <trkpt lat="43.903740" lon="20.224103">
        <ele>442.882</ele>
        <time>2021-07-28T13:39:40Z</time>
      </trkpt>
      <trkpt lat="43.903707" lon="20.223887">
        <ele>442.442</ele>
        <time>2021-07-28T13:42:00Z</time>
      </trkpt>
      <trkpt lat="43.903435" lon="20.223990">
        <ele>456.687</ele>
        <time>2021-07-28T13:42:28Z</time>
      </trkpt>
      <trkpt lat="43.904492" lon="20.224290">
        <ele>429.867</ele>
        <time>2021-07-28T13:43:56Z</time>
      </trkpt>
      <trkpt lat="43.904722" lon="20.224885">
        <ele>425.958</ele>
        <time>2021-07-28T13:44:43Z</time>
      </trkpt>
      <trkpt lat="43.905088" lon="20.224492">
        <ele>418.461</ele>
        <time>2021-07-28T13:45:30Z</time>
      </trkpt>
      <trkpt lat="43.905135" lon="20.224020">
        <ele>408.357</ele>
        <time>2021-07-28T13:46:48Z</time>
      </trkpt>
      <trkpt lat="43.905282" lon="20.224023">
        <ele>405.750</ele>
        <time>2021-07-28T13:46:57Z</time>
      </trkpt>
      <trkpt lat="43.905203" lon="20.223402">
        <ele>396.841</ele>
        <time>2021-07-28T13:47:32Z</time>
      </trkpt>
      <trkpt lat="43.905337" lon="20.222302">
        <ele>383.181</ele>
        <time>2021-07-28T13:48:37Z</time>
      </trkpt>
    </trkseg>
  </trk></gpx>""",
        photo="../../assets/mountain_logo.webp",
        price=500,
    )

    database.session.add(route3)
    database.session.commit()

    userRoute = UserRoute(userId=user.id, routeId=route1.id)
    database.session.add(userRoute)
    database.session.commit()

    userRoute = UserRoute(userId=user.id, routeId=route2.id)
    database.session.add(userRoute)
    database.session.commit()

    userRoute = UserRoute(userId=user.id, routeId=route3.id)
    database.session.add(userRoute)
    database.session.commit()

    peak1 = Peak(name='Ovcar vrh', elevation=985)
    database.session.add(peak1)
    database.session.commit()


    peakRoute = RoutePeak(routeId = route3.id, peakId = peak1.id)
    database.session.add(peakRoute)
    database.session.commit()

  