import flask
import os
import random

app = flask.Flask(__name__)

@app.route('/')

def index():
    num = random.randint(1, 20)
    birthday = '11/20/1998'
    return flask.render_template(
        "index.html", 
        random_number = num, #HTML var = python var
        birth_date = birthday
        )
    
app.run(
    port = int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)