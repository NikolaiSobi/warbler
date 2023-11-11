from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, EmailField, validators
from wtforms.validators import DataRequired, Email, Length


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""

    text = TextAreaField('text', validators=[DataRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    image_url = StringField('(Optional) Image URL')


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])

class UserEditForm(FlaskForm):
    """Edit user profile form"""

    username = StringField('Username')
    email = EmailField('E-mail', [validators.Optional()])
    image_url = StringField('Profile picture URL')
    header_image_url = StringField('Profile Header Picture URL')
    bio = TextAreaField('Bio')
    password = PasswordField('Password')

