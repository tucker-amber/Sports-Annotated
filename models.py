# beginning of models.py
# note that at this point you should have created "bookdb" database (see install_postgres.txt).
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres:Hello!123@localhost:5432/nfl')
db = SQLAlchemy(app)

class Nfl(db.Model):
	__tablename__ = 'players'
	id = db.Column(db.Integer, primary_key = True)
	jersey_num = db.Column(db.Integer, nullable = False)
	players = db.Column(db.String(80), nullable = False)
	age = db.Column(db.Integer, nullable = False)
	pos = db.Column(db.String(80), nullable = False)
	team = db.Column(db.String(80), nullable = False)
class Nfl2(db.Model):
	__tablename__ = "teams"
	id = db.Column(db.Integer, primary_key = True)
	stadium_name = db.Column(db.String(80), nullable = False)
	games_played = db.Column(db.Integer, nullable = False)
	city = db.Column(db.String(80), nullable = False)
	week = db.Column(db.Integer, nullable = False)
	team = db.Column(db.String(80), nullable = False)
	
class Nfl3(db.Model):
	__tablename__ = "weeks"
	id = db.Column(db.Integer, primary_key = True)
	week = db.Column(db.Integer, nullable = False)
	team = db.Column(db.String(80), nullable = False)
	
db.drop_all()
db.create_all()
# End of models.py