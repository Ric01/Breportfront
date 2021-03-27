from flaskfront import app,db
from flaskfront.models import User, ReportRequest
from flask_script import Manager,prompt_bool
from flaskfront.__init__ import db

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username="Ric",email="ricardo.suarez.atencio@gmail.com"))
    db.session.add(User(username="Lauri",email="sabatinimarialaura@gmail.com"))
    db.session.commit()
    print("Database initialized")

@manager.command
def dropdb():
    if prompt_bool(
        "Sure you want to erase all data?"):
        db.drop_all()
        print ("Dropped the database")


if __name__ == '__main__':
    manager.run()