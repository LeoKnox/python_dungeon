from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    roomData = [{"roomID":"1111","roomName":"Entry","material":"Stone","length":5,"width":5},
        {"roomID":"1112","roomName":"Throne","material":"Gold","length":7,"width":9},
        {"roomID":"1113","roomName":"Prison","material":"Iron","length":8,"width":6}]

    return render_template("index.html", dungeon="First", roomData = roomData, index=True)

@app.route("/login")
def login():
    return render_template("login.html", login=True)

@app.route("/room")
def room():
    return render_template("room.html", dungeon="First", room=True)

@app.route("/create")
def create():
    return render_template("create.html", create=True)