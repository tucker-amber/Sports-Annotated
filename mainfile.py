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
  for i in range(0,(len(week)+1)):
    if i == len(week):
      break
    if len(newList2) == 2:
      newList.append(newList2)
      newList2 = []
    if len(newList2) < 2:
      newList2.append(week[i])
  newList2.append(week[-2])
  newList2.append(week[-1])
  newList.append(newList2)
  return render_template('weeks.html' , week = newList) 
 
@app.route('/players/')
def players():
  players_ = db.session.query(Player).all()
  newDict = {}
  for i in players_:
    if i.pos in newDict:
      newDict[i.pos].append(i)
    else:
      newDict[i.pos] = [i]
  return render_template('players.html', playerss = newDict)

# Navigates to ind player's page
@app.route('/brady/<player_id>')
def brady(player_id):
  players_ = db.session.query(Player).filter_by(id = player_id).first()
  # for i in players:
    # if i.name == str(name):
      # player_name = i
  return render_template('brady.html', player = players_)
  
@app.route('/teams')
def teams():
  team = db.session.query(Teams).all()
  return render_template('teams.html', team = team)
 
# Navigates to Patriots page
@app.route('/teampage/<team_name>')
def teampage(team_name):
  team = db.session.query(Teams).filter_by(team = team_name).first()
  qb = db.session.query(Player).filter_by(pos = "QB").first()
  return render_template('teampage.html', team = team, qb = qb)


@app.route('/about')
def about():
  return render_template('about.html')
  
@app.route('/game/<team_name>')
def game(team_name):
  game = db.session.query(Weeks).all()
  newList = []
  newList2 = []
  for i in game:
    if len(newList2) == 2:
      newList.append(newList2)
      newList2 = []
    if len(newList2) <= 2:
      newList2.append(i)
  newList2.append(game[-2])
  newList2.append(game[-1])
  newList.append(newList2)
  for k in newList:
    if (k[0].team == team_name) or (k[1].team == team_name):
      a = k
  return render_template('gamepage.html', game = a)
  
# Navigates to Home/Splash page
@app.route('/splash')
def splash():
  return render_template('splash.html')

if __name__ == "__main__":
 app.run(debug = True)

 # This part is for Amber to use to connect to CS server :)
# app.run(host="128.83.144.118")
#----------------------------------------
# end of main2.py
#-----------------------------------------
