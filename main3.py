#-----------------------------------------
# main3.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template
from models import app, db, Nfl, Nfl2, Nfl3
from create_db import create_players
 
@app.route('/')
def index():
	return render_template('hello.html')

@app.route('/players/')
def player():
	players = db.session.query(Nfl).all()
	return render_template('books2.html', players = players)
	
if __name__ == "__main__":
	app.run()
# end of main3.py