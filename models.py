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
db.drop_all()
db.create_all()
# End of models.py