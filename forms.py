from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class SearchShelters(FlaskForm):
	streetname = StringField("What street are you in?", validators=[DataRequired()])
	storename = StringField("Do you see a store near you?", validators=[DataRequired()])
	dontknow = SubmitField("Don't Know Where I Am At")
	helpme = SubmitField("Help Me")

