from flask import Flask, render_template 
import datetime 
import calendar 
import pytz 

#Create a flask app
test = Flask(_name_)

#routing at '/'
@test.route('/')

def index():
    
current_time = datetime.datetime.now(pytz.timezone('Charlotte'))

ctime = current_time.strftime("%B %d %Y %H:%M:%S")

return render_template('index.html', ctime = calendar.day_name[current_time.weekday()] + ', ' +ctime)

if _name_ == '_main_':
    test.run()