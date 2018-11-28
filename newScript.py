from models import db, app, Player
import flask_whooshalchemy as wa

#--------------
#drops table
#Creates table
#--------------
db.drop_all()
db.create_all()
wa.whoosh_index(app, Player)
from create_db import create_players

