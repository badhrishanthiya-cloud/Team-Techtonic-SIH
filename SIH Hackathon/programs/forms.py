from programs import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, TextAreaField
from flask_wtf.file import FileAllowed


class LostForm(FlaskForm):
    name = StringField(label="Name")
    phone = StringField(label="Phone Number")
    hostel = StringField(label="Hostel name")
    loc = StringField(label="Approx. location where u might have lost (optional)")
    description = StringField(label="Description")
    submit = SubmitField(label="Search")


class FoundForm(FlaskForm):
    name = StringField(label="Name")
    phone = StringField(label="Phone Number")
    loc = StringField(label="Approx. location where u might have lost (optional)")
    description = StringField(label="Description")
    image = FileField("Upload Image", validators=[FileAllowed(["jpeg", "jpg", "png"])])
    submit = SubmitField(label="Submit response")


class QRForm(FlaskForm):
    name = StringField("Name")
    hostel = StringField("Hostel")
    phone = StringField("Phone")
    submit = SubmitField(label="Submit response")


class FeedbackForm(FlaskForm):
    name = StringField("Name (Optional)")
    message = TextAreaField(
        "Feedback",
    )
    submit = SubmitField("Send Feedback")
