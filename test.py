import os
import sys
import unittest
from models import app, db, Player, Teams, Weeks
from create_db import create_players, create_teams, create_weeks

class DBTestCases(unittest.TestCase):
	def setUp(self):
		app.config['Testing'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		app.config['DEBUG'] = False
		app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",
		'postgres://postgres:Hello!123@/postgres?host=35.226.209.166')
		self.app = app.test_client()

	# def test_source_insert_1(self):
		# s = Player(id ='1', jersey_num = 83, name = "Dwayne Allen", age = 28, pos = "TE", team = 'patriots')
		# db.session.add(s)
		# db.session.commit()
		# r = db.session.query(Player).filter_by(id = '1').one()
		# self.assertEqual(str(r.id), '1')
		# db.session.query(Player).filter_by(id = '1').delete()
		# db.session.commit()
	# def test_source_insert_2(self):
		# s = Player(id ='200', jersey_num = 600, name = "Ryan Allen 0", age = 28, pos = "P", team = 'patriots')
		# db.session.add(s)
		# db.session.commit()
		# r = db.session.query(Player).filter_by(id = '200').one()
		# self.assertEqual(str(r.id), '200')

		# db.session.query(Player).filter_by(id = '200').delete()
		# db.session.commit()
	# def test_source_insert_3(self):
		# s = Player(id ='300', jersey_num = 160, name = "Darren Andrews 0", age = 23, pos = "WR", team = 'patriots')
		# db.session.add(s)
		# db.session.commit()
		# r = db.session.query(Player).filter_by(id = '300').one()
		# self.assertEqual(str(r.id), '300')

		# db.session.query(Player).filter_by(id = '300').delete()
		# db.session.commit()
	
	# def test_team_source_insert_1(self):
		# s = Teams(id ='100', stadium_name = "Arrowhead Stadium", stadium_init = "ah", games_played = 368, city = "Kansas City", week = 1, team = 'chiefs')
		# db.session.add(s)
		# db.session.commit()
		# r = db.session.query(Teams).filter_by(id = '100').one()
		# self.assertEqual(str(r.id), '100')

		# db.session.query(Teams).filter_by(id = '100').delete()
		# db.session.commit()
	# def test_team_source_insert_2(self):
		# s = Teams(id ='200', stadium_name = "AT&T Stadium", stadium_init = "att", games_played = 80, city = "Arlington", week = 1, team = 'cowboys')
		# db.session.add(s)
		# db.session.commit()
		# r = db.session.query(Teams).filter_by(id = '200').one()
		# self.assertEqual(str(r.id), '200')

		# db.session.query(Teams).filter_by(id = '200').delete()
		# db.session.commit()
	# def test_team_source_insert_3(self):
		# s = Teams(id ='300', stadium_name = "Bank of America Stadium", stadium_init = "ba", games_played = 188, city = "Charlotte", week = 1, team = 'panthers')
		# db.session.add(s)
		# db.session.commit()
		# r = db.session.query(Teams).filter_by(id = '300').one()
		# self.assertEqual(str(r.id), '300')

		# db.session.query(Teams).filter_by(id = '300').delete()
		# db.session.commit()
	# def test_week_source_insert_1(self):
		# s = Weeks(id ='100', week = 1, team = "chiefs", score = 38, overtime = "No",injuries = 1)
		# db.session.add(s)
		# db.session.commit()
		# r = db.session.query(Weeks).filter_by(id = '100').one()
		# self.assertEqual(str(r.id), '100')

		# db.session.query(Weeks).filter_by(id = '100').delete()
		# db.session.commit()
	# def test_week_source_insert_2(self):
		# s = Weeks(id ='200', week = 1, team = "cowboys", score = 8, overtime = "No" ,injuries = 3)
		# db.session.add(s)
		# db.session.commit()
		# r = db.session.query(Weeks).filter_by(id = '200').one()
		# self.assertEqual(str(r.id), '200')

		# db.session.query(Weeks).filter_by(id = '200').delete()
		# db.session.commit()
	# def test_week_source_insert_3(self):
		# s = Weeks(id ='300', week = 1, team = "panthers", score = 16, overtime = "No",injuries = 5)
		# db.session.add(s)
		# db.session.commit()
		# r = db.session.query(Weeks).filter_by(id = '300').one()
		# self.assertEqual(str(r.id), '300')

		# db.session.query(Weeks).filter_by(id = '300').delete()
		# db.session.commit()

	## Complete test for db
	
	## Testing the page methods on mainfile.py
	
	def test_index_page(self):
		response = self.app.get('/', follow_redirects = True)
		self.assertEqual(response.status_code, 404)
		
	def test_search_page(self):
		response = self.app.get('/search/', follow_redirects = True)
		self.assertEqual(response.status_code, 404)
	
	def test_weeks_page(self):
		response = self.app.get('/weeks/', follow_redirects = True)
		self.assertEqual(response.status_code, 404)
	
	def test_players_page(self):
		response = self.app.get('/players/', follow_redirects = True)
		self.assertEqual(response.status_code, 404)
	
	def test_brady_page(self, id = 1):
		response = self.app.get('/brady/1/', follow_redirects = True)
		self.assertEqual(response.status_code, 404)
	
	def test_teams_page(self):
		response = self.app.get('/teams/', follow_redirects = True)
		self.assertEqual(response.status_code, 404)
		
	def test_teampage_page(self, team_name = 'patriots'):
		response = self.app.get('/teampage/patriots/', follow_redirects = True)
		self.assertEqual(response.status_code, 404)
	
	def test_about_page(self):
		response = self.app.get('/about/', follow_redirects = True)
		self.assertEqual(response.status_code, 404)
		
	def test_game_page(self, team_name = 'patriots'):
		response = self.app.get('/game/patriots/', follow_redirects = True)
		self.assertEqual(response.status_code, 404)
		
	def test_splash_page(self):
		response = self.app.get('/splash/', follow_redirects = True)
		self.assertEqual(response.status_code, 404)
	
	def test_test_page(self):
		response = self.app.get('/test/', follow_redirects = True)
		self.assertEqual(response.status_code, 404)
	
	def tearDown(self):
		pass
if __name__ == '__main__':
	unittest.main()

 