from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, Email

class NoteForm(FlaskForm):
    title = StringField("Title: ", validators=[DataRequired()])
    text = TextAreaField("Text: ")
    file = FileField("File: ",validators=[])
    submit = SubmitField("Submit")
    class Meta():
        csrf=False