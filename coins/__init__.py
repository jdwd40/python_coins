from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from coins.models.models import User, Coin, Transaction  # Add this line

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jd:K1ller1921@localhost/pcoinsdb'

    db.init_app(app)

    with app.app_context():  # Add this line
        @app.cli.command("reset_db")
        def reset_db():
            db.drop_all()
            db.create_all()
            print("Database reset.")
            
    return app



