from controllers.app import db  # Add this line at the top of your models.py
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)   # added username field
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    balance = db.Column(db.Float, default=200)

    # transactions = db.relationship('Transaction', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.email

class Coin(db.Model):
    __tablename__ = 'coins'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    symbol = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float, nullable=False)

    transactions = db.relationship('Transaction', backref='coin', lazy=True)

    def __repr__(self):
        return '<Coin %r>' % self.name

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    coin_id = db.Column(db.Integer, db.ForeignKey('coins.id'), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    price_per_coin = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return '<Transaction %r>' % self.id
