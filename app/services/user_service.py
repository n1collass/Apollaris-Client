from app.models.user import User
from app import db

class UserService:
    @staticmethod
    def create_user(name, email):
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def find_by_email(email):
        return User.query.filter_by(email=email).first()
