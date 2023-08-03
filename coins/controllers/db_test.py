from app import app, db

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Table created")
        db.session.commit()
        db.drop_all()
        print("Table dropped")

