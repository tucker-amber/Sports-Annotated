#!/usr/bin/env python3

# note that at this point you should have created nfl database (see install_postgres.txt).
#-----------------------------------------------------------------------------------------------
#Projects/IDB3/models.py
#CopyRight (C) 2016
#Jerry Han
#-----------------------------------------------------------------------------------------------

#--------------------------------------
#import flask library and other modules
#--------------------------------------
import flask
from flask import Flask, render_template, request
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy
import os
import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres:Hello!123@/postgres?host=35.226.209.166')
print(os.environ.get("DB_STRING",'postgres://postgres:Hello!123@/postgres?host=35.226.209.166'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['WHOOSH_BASE'] = 'whoosh'

db = SQLAlchemy(app)
#----------------
#Class Player
#----------------
class Player(db.Model):
	"""
	reads in a database as an argument. Note this is a class
	access the db by calling on a specific table: players
	assign id, jersey_num, name, age, pos, team to their own data
	
	The __searchable__ uses whoosh_alchemy to be able to search
	the db on certain columns listed in its list data structure
	"""
	
	__tablename__ = 'players'
	__searchable__ = ['id','name', 'pos', 'team']
	id = db.Column(db.Integer, primary_key = True)
	jersey_num = db.Column(db.Integer, nullable = False)
	name = db.Column(db.String(80), nullable = False)
	age = db.Column(db.Integer, nullable = False)
	pos = db.Column(db.String(80), nullable = False)
	team = db.Column(db.String(80), nullable = False)

#----------------
#Class Teams
#----------------
class Teams(db.Model):
	"""
	reads in a database as an argument. Note this is a class
	access the db by calling on a specific table: teams
	assign id, stadium_name, stadium_init, games_played, city, week,
	team to their own data
	"""
	__tablename__ = "teams"
	id = db.Column(db.Integer, primary_key = True)
	stadium_name = db.Column(db.String(80), nullable = False)
	stadium_init = db.Column(db.String(80), nullable = False)
	games_played = db.Column(db.Integer, nullable = False)
	city = db.Column(db.String(80), nullable = False)
	week = db.Column(db.Integer, nullable = False)
	team = db.Column(db.String(80), nullable = False)
	
#----------------
#Class Weeks
#----------------
class Weeks(db.Model):
	"""
	reads in a database as an argument. Note this is a class
	access the db by calling on a specific table: Weeks
	assign id, week, team, score, overtime, injuries to their own data
	"""
	__tablename__ = "weeks"
	id = db.Column(db.Integer, primary_key = True)
	week = db.Column(db.Integer, nullable = False)
	team = db.Column(db.String(80), nullable = False)
	score = db.Column(db.Integer, nullable = False)
	overtime = db.Column(db.String(80), nullable = False)
	injuries = db.Column(db.Integer, nullable = False)

# db.drop_all()
# db.create_all()


# End of models.py
