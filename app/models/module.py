from app import db
from datetime import datetime

class Module(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    ocv = db.Column(db.Float)
    scc = db.Column(db.Float)

    def __repr__(self):
        return f"<User {self.name}>"