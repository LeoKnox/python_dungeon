from application import app, db
from flask import render_template, request, json

roomData = [{"roomID":"1111","roomName":"Entry","material":"Stone","length":5,"width":5},
    {"roomID":"1112","roomName":"Throne","material":"Gold","length":7,"width":9},
    {"roomID":"1113","roomName":"Prison","material":"Iron","length":8,"width":6}]

@app.route("/")
@app.route("/index")
@app.route("/index/<dungeon>")
def index(dungeon="First"):
    return render_template("index.html", dungeon=dungeon, roomData = roomData, index=True)

@app.route("/login")
def login():
    return render_template("login.html", login=True)

@app.route("/room")
def room():
    return render_template("room.html", dungeon="First", room=True)

@app.route("/create")
def create():
    return render_template("create.html", create=True)

@app.route("/edit", methods=["GET","POST"])
def edit():
    roomID = request.form.get('roomID')
    roomName = request.form.get('roomName')
    material = request.form.get('material')
    return render_template("edit.html", data={"roomID":roomID, "roomName":roomName, "material":material})