from flask_wtf import Form
from wtforms.fields import StringField,SubmitField,PasswordField,BooleanField
from wtforms import RadioField,validators
from wtforms.validators import DataRequired, url,input_required

class ReportForm(Form):
    report_type = RadioField(
        'Tipo de reporte:', choices=[('simple_report', 'Reporte Simple'), ('agg_report', 'Reporte Agregado')])
    company_list = StringField(u'Company List:', validators=[validators.input_required()])
    email = StringField(u'email:', validators=[validators.input_required()])
    submit = SubmitField('Generar')

class LoginForm(Form):
    username = StringField('Usuario: ',validators=[DataRequired()])
    password = PasswordField('Contraseña:', validators=[DataRequired()])
    remember_me = BooleanField ('Mantenerme conectado')
    submit = SubmitField('Ingresar')