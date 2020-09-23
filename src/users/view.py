from flask import Blueprint, jsonify, request
from users.service import UserService
from users.mappers import *

user_api = Blueprint('user_api', __name__)
service = UserService()

@user_api.route('/', methods=['GET'])
def get_users():
  user_list = service.list_()
  
  return jsonify(user_list)

@user_api.route('/', methods=['POST'])
def post_user():
  created_user = service.insert(request.get_json())

  return jsonify({'id': str(created_user.id)})
