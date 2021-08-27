from flask_wtf import FlaskForm, CSRFProtect
from wtforms import SubmitField

class subMit(FlaskForm):
	submit = SubmitField('Shorten')