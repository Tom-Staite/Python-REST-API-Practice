from db import db

class UserModel(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(80), unique=True, nullable=False)
    pwd = db.Column(db.String, nullable=False)