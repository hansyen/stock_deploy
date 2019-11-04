from flask_wtf import FlaskForm
from wtforms import SelectField, StringField


class UserInfoSearchForm(FlaskForm):
    choices = [('uid', 'User ID'),
               ('family_name', 'Family Name'),
               ('first_name', 'First Name')]
    select = SelectField('Search for User Info:', choices=choices)
    search = StringField('')