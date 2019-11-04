from flask_wtf import FlaskForm
from wtforms import SelectField, StringField


class WalletLogSearchForm(FlaskForm):
    choices = [('uid', 'User ID'),
               ('tid', 'Ticket Number'),
               ('log_type', 'Log Type'),
               ('status', 'Status')]
    select = SelectField('Search for DC Trade Log:', choices=choices)
    search = StringField('')