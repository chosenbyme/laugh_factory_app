from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Comment(db.Model):
    __tablename__ = "comments"

    id= db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer)
    comment = db.Column(db.String(250))

class User(db.Model):
    __tablename__ = "users"

    id= db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    email = db.Column(db.String(30))
    password = db.Column(db.String(20))
