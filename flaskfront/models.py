from datetime import datetime
from flask_login import UserMixin
from . import db


class ReportRequest(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime, default = datetime.utcnow())
    report_type = db.Column(db.String(120),unique=False,nullable=False)
    company_list = db.Column(db.String(900),unique=False)

    def __repr__(self):
        return "<Request '{}':'{}'/ '{}'>".format(self.id,self.date,self.company_name)

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True)
    email = db.Column(db.String(120),unique=True)

    def __repr__(self):
        return '<User %r>' % self.username
    

