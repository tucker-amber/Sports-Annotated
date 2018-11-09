# beginning of models.py
# note that at this point you should have created "bookdb" database (see install_postgres.txt).
from flask import Flask, render_template, request
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import os
import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres:Hello!123@localhost:5432/nfl')
db = SQLAlchemy(app)
CORS(app)
manager = APIManager(app, flask_sqlalchemy_db = db)

class Player(db.Model):
	__tablename__ = 'player'
	id = db.Column(db.Integer, primary_key = True)
	jersey_num = db.Column(db.Integer, nullable = False)
	name = db.Column(db.String(80), nullable = False)
	age = db.Column(db.Integer, nullable = False)
	pos = db.Column(db.String(80), nullable = False)
	team = db.Column(db.String(80), nullable = False)

class Teams(db.Model):
	__tablename__ = "teams"
	id = db.Column(db.Integer, primary_key = True)
	stadium_name = db.Column(db.String(80), nullable = False)
	stadium_init = db.Column(db.String(80), nullable = False)
	games_played = db.Column(db.Integer, nullable = False)
	city = db.Column(db.String(80), nullable = False)
	week = db.Column(db.Integer, nullable = False)
	team = db.Column(db.String(80), nullable = False)
	
class Weeks(db.Model):
	__tablename__ = "weeks"
	id = db.Column(db.Integer, primary_key = True)
	week = db.Column(db.Integer, nullable = False)
	team = db.Column(db.String(80), nullable = False)
	score = db.Column(db.Integer, nullable = False)
	overtime = db.Column(db.String(80), nullable = False)
	injuries = db.Column(db.Integer, nullable = False)

# class Player_Week(db.Model):
# __tablename__ = "player/Weeks"
	
# player_week_id = db.Column(
	
#db.drop_all()
db.create_all()

manager.create_api(Player, methods=['GET'], url_prefix = None)
manager.create_api(Teams, methods=['GET'], url_prefix = None)
manager.create_api(Weeks, methods=['GET'], url_prefix = None)
# End of models.py