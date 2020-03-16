from application import app, db
from flask import render_template, request, json, redirect, flash
from application.models import Character, Room, Location
from application.forms import LoginForm, CreateForm

roomData = [{"roomID":"1111","roomName":"Entry","material":"Stone","length":5,"width":5},
    {"roomID":"1112","roomName":"Throne","material":"Gold","length":7,"width":9},
    {"roomID":"1113","roomName":"Prison","material":"Iron","length":8,"width":6}]

@app.route("/")
@app.route("/index")
@app.route("/index/<dungeon>")
def index(dungeon="First"):
    rooms = Room.objects.all()
    print(rooms[0].room_name)
    return render_template("index.html", dungeon=dungeon, roomData = rooms, index=True)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        character_name = form.character_name.data
        character_id = form.character_id.data
        character = Character.objects(character_name=character_name).first()
        print (int(character_id) == character.character_id)
        print (character_id)
        if character and int(character_id) == character.character_id:
            flash(f"{character.character_name}, You are ready for adventure!")
            return redirect("/index")
        else:
            flash("Wrong, go create someone.")
    return render_template("login.html", form=form, login=True)

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

@app.route("/character")
def character():
    #Character(character_id=1, character_name="Aelien", character_class="Fighter", race="Human",
    #atk=10, def=15, health=35).save()
    #Character(character_id=2, character_name="Eveehi", character_class="Rogue", race="Elf",
    #atk=14, def=12, health=20).save()
    characters = Character.objects.all()
    return render_template("character.html", characters=characters)