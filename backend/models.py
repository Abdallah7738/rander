from config import db
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.string(80), unique=False, nullable=False)
    last_name = db.Column(db.string(80), unique=False, nullable=False)
    email = db.Column (db.string(120), unique=True, nullable=False)
    
    
    