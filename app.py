from flask import Flask

from pb_user import update_user as update_user_handler
from pb_user import detail_user as detail_user_handler
from pb_user import delete_user as delete_user_handler
from pb_user import create_user as create_user_handler
from pb_user import list_user as list_user_handler

app = Flask(__name__)


@app.route('/users', methods=['GET'])
def list_user():
    return list_user_handler()


@app.route('/user/<user_id>', methods=['GET'])
def detail_user(user_id):
    return detail_user_handler(user_id)


@app.route('/user', methods=['POST'])
def create_user():
    return create_user_handler()


@app.route('/user/<user_id>', methods=['PATCH'])
def update_user(user_id):
    return update_user_handler(user_id)


@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    return delete_user_handler(user_id)
