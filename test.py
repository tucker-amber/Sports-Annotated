import os
import sys
import unittest
from models import db, Player, Teams, Weeks

class DBTestCases(unittest.TestCase):
	def test_source_insert_1(self):
		s = Player(id ='1', jersey_num = 83, name = "Dwayne Allen", age = 28, pos = "TE", team = 'patriots')
		db.session.add(s)
		db.session.commit()
		r = db.session.query(Player).filter_by(id = '1').one()
		self.assertEqual(str(r.id), '1')

		db.session.query(Player).filter_by(id = '1').delete()
		db.session.commit()
	def test_source_insert_2(self):
		s = Player(id ='2', jersey_num = 6, name = "Ryan Allen", age = 28, pos = "P", team = 'patriots')
		db.session.add(s)
		db.session.commit()
		r = db.session.query(Player).filter_by(id = '2').one()
		self.assertEqual(str(r.id), '2')

		db.session.query(Player).filter_by(id = '2').delete()
		db.session.commit()
	def test_source_insert_3(self):
		s = Player(id ='3', jersey_num = 16, name = "Darren Andrews", age = 23, pos = "WR", team = 'patriots')
		db.session.add(s)
		db.session.commit()
		r = db.session.query(Player).filter_by(id = '3').one()
		self.assertEqual(str(r.id), '3')

		db.session.query(Player).filter_by(id = '3').delete()
		db.session.commit()
	
	def test_team_source_1(self):
		s = Teams(id ='1', stadium_name = "Arrowhead Stadium", stadium_init = "ah", games_played = 368, city = "Kansas City", week = 1, team = 'chiefs')
		db.session.add(s)
		db.session.commit()
		r = db.session.query(Teams).filter_by(id = '1').one()
		self.assertEqual(str(r.id), '1')

		db.session.query(Teams).filter_by(id = '1').delete()
		db.session.commit()
	def test_team_source_2(self):
		s = Teams(id ='2', stadium_name = "AT&T Stadium", stadium_init = "att", games_played = 80, city = "Arlington", week = 1, team = 'cowboys')
		db.session.add(s)
		db.session.commit()
		r = db.session.query(Teams).filter_by(id = '2').one()
		self.assertEqual(str(r.id), '2')

		db.session.query(Teams).filter_by(id = '2').delete()
		db.session.commit()
	def test_team_source_3(self):
		s = Teams(id ='3', stadium_name = "Bank of America Stadium", stadium_init = "ba", games_played = 188, city = "Charlotte", week = 1, team = 'panthers')
		db.session.add(s)
		db.session.commit()
		r = db.session.query(Teams).filter_by(id = '3').one()
		self.assertEqual(str(r.id), '3')

		db.session.query(Teams).filter_by(id = '3').delete()
		db.session.commit()
	def test_week_source_1(self):
		s = Weeks(id ='1', week = 1, team = "chiefs", score = 38, overtime = "No",injuries = 1)
		db.session.add(s)
		db.session.commit()
		r = db.session.query(Weeks).filter_by(id = '1').one()
		self.assertEqual(str(r.id), '1')

		db.session.query(Weeks).filter_by(id = '1').delete()
		db.session.commit()
	def test_week_source_2(self):
		s = Weeks(id ='2', week = 1, team = "cowboys", score = 8, overtime = "No" ,injuries = 3)
		db.session.add(s)
		db.session.commit()
		r = db.session.query(Weeks).filter_by(id = '2').one()
		self.assertEqual(str(r.id), '2')

		db.session.query(Weeks).filter_by(id = '1').delete()
		db.session.commit()
	def test_week_source_3(self):
		s = Weeks(id ='3', week = 1, team = "panthers", score = 16, overtime = "No",injuries = 5)
		db.session.add(s)
		db.session.commit()
		r = db.session.query(Weeks).filter_by(id = '3').one()
		self.assertEqual(str(r.id), '3')

		db.session.query(Weeks).filter_by(id = '3').delete()
		db.session.commit()

if __name__ == '__main__':
 unittest.main()