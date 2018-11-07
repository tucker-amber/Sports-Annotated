#-----------------------------------------
# main3.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template
from models import app, db, Nfl
from create_db import create_players
app = Flask(__name__)

#books = [{'title': 'Software Engineering', 'id': '1'}, \
 #{'title':'Algorithm Design', 'id':'2'}, \
 #{'title':'Python', 'id':'3'}] \
 
@app.route('/')
def index():
	return render_template('hello.html')
@app.route('/book2/')
def book():
	players = db.session.query(Nfl).all()
	return render_template('books2.html', books = books)
	
if __name__ == "__main__":
	app.run()
# end of main3.py