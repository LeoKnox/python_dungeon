from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    character_id    =   StringField( validators=[DataRequired()])
    character_name  =   StringField( validators=[DataRequired()])
    remember_me     =   BooleanField("Remember Me")
    submit          =   SubmitField("Login")

class CreateForm(FlaskForm):
    character_id    =   StringField("ID", validators=[DataRequired()])
    character_name  =   StringField("Name", validators=[DataRequired()])
    character_class =   StringField("Class", validators=[DataRequired()])
    character_race  =   StringField("Race", validators=[DataRequired()])
    character_atk   =   IntField("Atk", validators=[DataRequired()])
    character_def   =   IntField("Def", validators=[DataRequired()])
    character_health=   IntField("Health", validators=[DataRequired()])