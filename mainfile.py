#-----------------------------------------
# mainfile.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template, request, redirect
#from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy
from models import app, db, Player, Teams, Weeks
import flask_whooshalchemy as wa
import os
import requests
import subprocess
import platform

wa.whoosh_index(app, Player)

@app.route('/')
def index():
  return render_template('splash.html')
  
# search function
@app.route('/search/')
@app.route('/splash/search')
def search():
  searches = Player.query.whoosh_search(request.args.get('query')).all()
  if not searches:
    searches = None
  return render_template('search.html', searches=searches)
  
# Navigates to weeks page
@app.route('/weeks/')
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
 
# Navigates to players page
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
  return render_template('brady.html', player = players_)

# Navigates to teams page
@app.route('/teams/')
def teams():
  team = db.session.query(Teams).all()
  return render_template('teams.html', team = team)

# Navigates to Patriots page
@app.route('/teampage/<team_name>')
def teampage(team_name):
  team = db.session.query(Teams).filter_by(team = team_name).first()
  qb = db.session.query(Player).filter_by(pos = "QB").first()
  return render_template('teampage.html', team = team, qb = qb)

#Navigates to about page
@app.route('/about/')
def about():
  return render_template('about.html')
  
# Navigates to game page
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
      game = k
  return render_template('gamepage.html', game = game)
  
# Navigates to Home/Splash page
@app.route('/splash/')
def splash():
  return render_template('splash.html')
  
# Navigates to unit test page
@app.route('/test/')
def test():
# Checks to see if the OS is Windows/Linux system
  if platform.system() == 'Windows':
    process = subprocess.Popen(["python", "-m", "coverage", "run", "--branch", "test.py"],
                              stdout=subprocess.PIPE,
							  stderr=subprocess.PIPE,
							  stdin=subprocess.PIPE)

  else:
    process = subprocess.Popen(["python3", "-m", "coverage", "run", "--branch", "test.py"],
                              stdout=subprocess.PIPE,
							  stderr=subprocess.PIPE,
							  stdin=subprocess.PIPE)

  out, err = process.communicate()
  output=err+out
  output = output.decode("utf-8")
  return render_template('test.html', output = "\n".join(output.split("\n")))


if __name__ == "__main__":
 app.run()

