from models.models import User, Coin, Transaction
from coins.controllers.app import db, app

# Create tables
with app.app_context():
    db.create_all()

# You can also add some initial data if you want. For example:
coins = [
    Coin(name='Bitcoin', symbol='BTC', price=45000.00),
    Coin(name='Ethereum', symbol='ETH', price=3000.00),
    Coin(name='Litecoin', symbol='LTC', price=150.00),
    Coin(name='Dogecoin', symbol='DOGE', price=0.25),
    Coin(name='Cardano', symbol='ADA', price=2.00)
]
db.session.bulk_save_objects(coins)
db.session.commit()

