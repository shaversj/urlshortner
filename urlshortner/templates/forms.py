from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import URL


class URLForm(FlaskForm):
    url = StringField("url", validators=[URL()])
    submit = SubmitField("Submit")


# Implement Flash Messaging to return TinyURL
