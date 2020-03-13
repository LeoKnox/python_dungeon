from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", dungeon="First")

@app.route("/login")
def login():
    return render_template("index.html", dungeon="First")

@app.route("/room")
def room():
    return render_template("index.html", dungeon="First")