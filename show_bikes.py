# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../moto2017-12-06T13.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'listings'

    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String, unique=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    location = db.Column(db.String)
    cl_id = db.Column(db.Integer, unique=True)

    def __repr__(self):
        print('duh')
        return '<url %r>' % self.name


