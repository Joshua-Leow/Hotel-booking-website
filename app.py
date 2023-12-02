from app import app, db
from flask import request, render_template
from flask_login import login_required, current_user

from controllers.auth import auth
from controllers.booking import booking
from controllers.chart import chart

from models.rooms import RoomType
from models.amenities import AmenityType
from models.beds import BedType
from models.users import User

# Register Blueprint so we can include the routes
app.register_blueprint(auth)
app.register_blueprint(booking)
app.register_blueprint(chart)

@app.route("/about", methods=["GET"])
@app.route("/", methods=["GET"])
def about():
    return render_template("about.html", panel="about us")


@app.route("/rooms", methods=["GET"])
def Rooms():
    all_room_types = RoomType.getAllRoomTypes()
    all_bed_types = BedType.getAllBedTypes()
    return render_template('rooms.html', panel="choice of room and bed", all_room_types=all_room_types, all_bed_types=all_bed_types)


@app.route("/amenities", methods=["GET"])
def Amenities():
    all_amenity_types = AmenityType.getAllAmenitiesTypes()
    return render_template('amenities.html', panel="choice of amenities", all_amenity_types=all_amenity_types)

