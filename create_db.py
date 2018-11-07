# beginning of create_db.py
import json
from models import db, Nfl, Nfl2, Nfl3

def load_json(filename):
	with open(filename) as file:
		jsn = json.load(file)
		file.close()
	return jsn

def create_players():
	player = load_json('players.json')
	for onePlayer in player:
		team = onePlayer['team']
		pos = onePlayer['pos']
		age = onePlayer['age']
		players_ = onePlayer['player']
		jersey_num = onePlayer['jersey_num']
		id = onePlayer['id']
		newBook = Nfl(id = id, jersey_num = jersey_num, players = players_, age = age, pos = pos,team = team)
		# After I create the book, I can then add it to my session.
		db.session.add(newBook)
		# commit the session to my DB.
		db.session.commit()
def create_teams():
	team = load_json('teams.json')
	for oneTeam in team:
		week = oneTeam['week']
		team = oneTeam['team']
		city = oneTeam['city']
		games_played = oneTeam['games_played']
		stadium_name = oneTeam['stadium_name']
		id = oneTeam['id']
		newTeam = Nfl2(id = id, stadium_name = stadium_name, games_played = games_played, city = city, team = team, week= week)
		# After I create the book, I can then add it to my session.
		db.session.add(newTeam)
		# commit the session to my DB.
		db.session.commit()

def create_weeks():
	week = load_json('weeks.json')
	for oneWeek in week:
		week = oneWeek['week']
		team = oneWeek['team']
		id = oneWeek['id']
		newWeek = Nfl3(id = id, team = team, week = week)
		# After I create the book, I can then add it to my session.
		db.session.add(newWeek)
		# commit the session to my DB.
		db.session.commit()		
create_players()
create_teams()
create_weeks()
# end of create_db.py