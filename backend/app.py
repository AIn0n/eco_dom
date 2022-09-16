from flask import Flask, request, make_response # basics for building APIs
from flask_cors import CORS # enable cross origin 
import pg8000.native        # postgresql wrapper for python

PASSWORD = "123"

app = Flask(__name__)
CORS(app)
db = pg8000.native.Connection("postgres", password=PASSWORD)

@app.route("/create_room", methods = ["POST"])
def create_rooom():
    name = request.form['name']
    print(name)
    db.run("INSERT INTO rooms (name) VALUES (:n)", n=name)
    return "OK"

@app.route("/delete_room", methods = ["DELETE"])
def delete_room():
    name = request.form['name']
    db.run("DELETE FROM rooms WHERE name = (:n)", n=name)
    return "OK"

@app.route("/rooms", methods = ["GET"])
def retrieve_rooms():
    result = []
    for name in db.run("SELECT (name) from rooms"):
        result.append(name)
    res = make_response(result, 200)
    return res