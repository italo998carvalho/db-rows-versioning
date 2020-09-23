from flask import Blueprint, jsonify, request
from users.repository import UserRepository
from users.mappers import *

user_api = Blueprint('user_api', __name__)
user_repository = UserRepository()

@user_api.route('/', methods=['GET'])
def get_users():
  user_list = to_dict_list(user_repository.get_all())
  
  return jsonify(user_list)

@user_api.route('/', methods=['POST'])
def post_user():
  data = request.get_json()

  user = to_object(data)
  created_user = user_repository.create(user)

  return jsonify({'id': str(created_user.id)})
