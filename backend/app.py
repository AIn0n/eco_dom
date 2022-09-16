from flask import Flask, request
import pg8000.native

PASSWORD = "123"

app = Flask(__name__)
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
