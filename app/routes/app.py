from flask import Blueprint
from app.controllers import user_controller

from app.middlewares.auth import auth_required

app = Blueprint('app', __name__)

@app.route('/users', methods=['GET'])
def index():
    return user_controller.list_users()

@app.route('/users', methods=['POST'])
def store():
    return user_controller.create_user()

@app.route('/protected', methods=['GET'])
@auth_required
def protected():
    return {'message': 'This is protected!'}
