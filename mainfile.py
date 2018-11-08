#-----------------------------------------
# mainfile.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template, request
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from models import app, db, Player, Teams, Weeks
from create_db import create_players
import os
import requests
#app = Flask(__name__)


@app.route('/')
def index():
  return render_template('splash.html')

  
@app.route('/weeks')
def weeks():
  week = db.session.query(Weeks).all()
  newList = []
  newList2 = []
  for i in week:
    if len(newList2) == 2:
      newList.append(newList2)
      newList2 = []
    else:
      newList2.append(i)

  return render_template('weeks.html' , week = newList) 


  
@app.route('/players/')
def players():
  players = db.session.query(Player).all()
  newDict = {}
  for i in players:
    if i.pos in newDict:
      newDict[i.pos].append(i)
    else:
      newDict[i.pos] = [i]
  return render_template('players.html', playerss = newDict)

  

# Navigates to ind player's page
@app.route('/brady/<integer:player_id>')
def brady(player_id):
  players = db.session.query(Player).filter_by(id = player_id)
  # for i in players:
    # if i.name == str(name):
      # player_name = i
  return render_template('brady.html', player = players)


  
@app.route('/teams')
def teams():
  team = db.session.query(Teams).all()
  return render_template('teams.html', team = team)
 
 

# Navigates to Patriots page
@app.route('/patriots')
def patriots():
  return render_template('patriots.html')

# Navigates to Cowboys page
# @app.route('/cowboys')
# def cowboys():
  # return render_template('cowboys.html')

# # Navigates to Cowboys page
# @app.route('/packers')
# def packers():
  # return render_template('packers.html')

@app.route('/about')
def about():
  return render_template('about.html')
  
@app.route('/game1')
def game1():
  return render_template('game1.html')
  
@app.route('/game2')
def game2():
  return render_template('game2.html')
  
@app.route('/game3')
def game3():
  return render_template('game3.html')


# Navigates to Home/Splash page
@app.route('/splash')
def splash():
  return render_template('splash.html')

if __name__ == "__main__":
 app.run()

 # This part is for Amber to use to connect to CS server :)
# app.run(host="128.83.144.118")
#----------------------------------------
# end of main2.py
#-----------------------------------------
