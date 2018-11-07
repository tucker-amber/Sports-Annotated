# beginning of create_db.py
import json
from models import db, Nfl

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
create_players()
# end of create_db.py