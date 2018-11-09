# beginning of create_db.py
import json
from models import db, Player, Teams, Weeks

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
		name = onePlayer['player']
		jersey_num = onePlayer['jersey_num']
		id = onePlayer['id']
		newBook = Player(id = id, jersey_num = jersey_num, name = name, age = age, pos = pos,team = team)
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
		stadium_init = oneTeam['stadium_init']
		stadium_name = oneTeam['stadium_name']
		id = oneTeam['id']
		newTeam = Teams(id = id, stadium_name = stadium_name, stadium_init = stadium_init, games_played = games_played, city = city, team = team, week= week)
		# After I create the book, I can then add it to my session.
		db.session.add(newTeam)
		# commit the session to my DB.
		db.session.commit()

def create_weeks():
	week = load_json('weeks.json')
	for oneWeek in week:
		score = oneWeek['score']
		week = oneWeek['week']
		team = oneWeek['team']
		id = oneWeek['id']
		overtime = oneWeek['overtime']
		injuries = oneWeek['injuries']
		newWeek = Weeks(id = id, team = team, week = week, score = score, overtime = overtime, injuries = injuries)
		# After I create the book, I can then add it to my session.
		db.session.add(newWeek)
		# commit the session to my DB.
		db.session.commit()		
create_players()
create_teams()
create_weeks()
# end of create_db.py