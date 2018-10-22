#-----------------------------------------
# mainfile.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('splash.html')


@app.route('/weeks')
def weeks():
  return render_template('weeks.html') 

@app.route('/players')
def players():
  return render_template('players.html')

@app.route('/teams')
def teams():
  return render_template('teams.html')
 
@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == "__main__":
 app.run()
#----------------------------------------
# end of main2.py
#-----------------------------------------
