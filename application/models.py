import flask
from application import db

class Character(db.Document):
    character_id    =   db.IntField( unique=True )
    character_name  =   db.StringField( max_length=50, unique=True)
    character_class =   db.StringField( max_length=50 )
    character_race  =   db.StringField( max_length=50 )
    character_atk   =   db.IntField()
    character_def   =   db.IntField()
    character_health=   db.IntField()

class Room(db.Document):
    room_id         =   db.StringField( max_length=10, unique=True )
    room_name       =   db.StringField( max_length=50, unique=True )
    room_type       =   db.StringField( max_length=50 )
    room_length     =   db.IntField()
    room_width      =   db.IntField()

class Location(db.Document):
    character_id    =   db.IntField()
    room_id         =   db.StringField( max_length=10 )