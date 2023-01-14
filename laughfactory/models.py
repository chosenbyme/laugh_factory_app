# ignore this code for now. wait until database tested

from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Comment(db.Model):
    __tablename__ = 'users'

    id= db.Column(db.Integer, primary_key = True)
    submitter = db.Column(db.String(250))
    comment = db.Column(db.Text)

    __tablename__ = 'comments'

    id= db.Column(db.Integer, primary_key = True)
    submitter = db.Column(db.String(250))
    comment = db.Column(db.Text)
