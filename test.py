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

if __name__ == '__main__':
 unittest.main()