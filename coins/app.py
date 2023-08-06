from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jd:K1ller1921@localhost/pcoinsdb'
db = SQLAlchemy(app)

@app.route('/yo')
def hello_world():
    return '<h1>Hello, World!</h1>'


