from datetime import datetime
from sqlite3 import DatabaseError
from flask import Flask, request, make_response # basics for building APIs
from flask_cors import CORS # enable cross origin 
import pg8000.native        # postgresql wrapper for python
import time                 # date conversion

PASSWORD = "123"

app = Flask(__name__)
CORS(app)
db = pg8000.native.Connection("postgres", password=PASSWORD)

@app.route("/create_room", methods = ["POST"])
def create_rooom():
    name = request.form['name']
    print(name)
    try:
        db.run("INSERT INTO rooms (name) VALUES (:n)", n=name)
    except DatabaseError:
        return make_response("something go wrong in database", "500")
    return "OK"

@app.route("/delete_room", methods = ["DELETE"])
def delete_room():
    name = request.form['name']
    db.run("DELETE FROM rooms WHERE name = (:n)", n=name)
    return "OK"

@app.route("/rooms", methods = ["GET"])
def retrieve_rooms():
    result = []
    for elem in db.run("SELECT * from rooms"):
        result.append({"id" : elem[0], "name" : elem[1]})
    res = make_response(result, 200)
    return res

@app.route("/room/<id>/devices", methods = ["GET"])
def retrieve_devicies_from_room(id):
    result = []
    for x in db.run("SELECT * FROM devices WHERE room_id = (:id)", id=id):
        result.append({"id" : x[0], "name" : x[1], "power": x[2], "start_time" : x[3].strftime("%H:%M"), "end_time" : x[4].strftime("%H:%M"), "energy_class" : x[5], "room_id" : x[6]})
    return result
