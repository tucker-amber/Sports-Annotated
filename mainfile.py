#-----------------------------------------
# mainfile.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
 return render_template('splash.html')
<<<<<<< HEAD

 #@app.route('')

def teams():
 #return render_template('team.html')
  pass
@app.route('/weeks/')
def weeks():
 return render_template('weeks.html') 

=======

@app.route('/players')
def players():
  return render_template('players.html')

@app.route('/teams')
def teams():
 return render_template('teams.html')

@app.route('/weeks')
def weeks():
  return render_template('weeks.html')

#def weeks():
# return render_template('weeks.html')
# pass
>>>>>>> bf55808fe8a2f87c3f150209d0c009c4a8fdb3f8
if __name__ == "__main__":
 app.run()
#----------------------------------------
# end of main2.py
#-----------------------------------------
