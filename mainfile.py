#-----------------------------------------
# mainfile.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
 return render_template('first_page.html')

@app.route('/teams')
def teams():
 return render_template('teams.html')

#def weeks():
 #return render_template('weeks.html')
 #pass
if __name__ == "__main__":
 app.run()
#----------------------------------------
# end of main2.py
#-----------------------------------------
