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

# Navigates to ind player's page
@app.route('/hoyer')
def hoyer():
  return render_template('hoyer.html')

# Navigates to ind player's page
@app.route('/brady')
def brady():
  return render_template('brady.html')

# Navigates to ind player's page
@app.route('/barner')
def barner():
  return render_template('barner.html')

@app.route('/teams')
def teams():
  return render_template('teams.html')
 
# Navigates to Patriots page
@app.route('/patriots')
def patriots():
  return render_template('patriots.html')

# Navigates to Cowboys page
@app.route('/cowboys')
def cowboys():
  return render_template('cowboys.html')

# Navigates to Cowboys page
@app.route('/packers')
def packers():
  return render_template('packers.html')

@app.route('/about')
def about():
  return render_template('about.html')
  
@app.route('/game1')
def game1():
  return render_template('game1.html')
  
@app.route('/game2')
def game2():
  return render_template('game2.html')
  
@app.route('/game3')
def game3():
  return render_template('game3.html')


# Navigates to Home/Splash page
@app.route('/splash')
def splash():
  return render_template('splash.html')

if __name__ == "__main__":
 app.run()

 # This part is for Amber to use to connect to CS server :)
# app.run(host="128.83.144.118")
#----------------------------------------
# end of main2.py
#-----------------------------------------
