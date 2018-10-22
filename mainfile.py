#-----------------------------------------
# mainfile.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
 return render_template('splash.html')

 #@app.route('')

def teams():
 #return render_template('team.html')
  pass
@app.route('/weeks/')
def weeks():
 return render_template('weeks.html') 

if __name__ == "__main__":
 app.run()
#----------------------------------------
# end of main2.py
#----------------------------------------- 