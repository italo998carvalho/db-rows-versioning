from flask import Blueprint, jsonify, request
from users.service import UserService
from users.mappers import *

user_api = Blueprint('user_api', __name__)
service = UserService()

@user_api.route('/', methods=['GET'])
def get_users():
  user_list = service.get_all()
  return jsonify(user_list), 200

@user_api.route('/<id>', methods=['GET'])
def get_user(id):
  user = service.get_one(id)
  return jsonify(user), 200

@user_api.route('/', methods=['POST'])
def post_user():
  data = request.get_json()
  created_user = service.insert(data)
  return jsonify({'id': str(created_user.id)}), 201

@user_api.route('/<id>', methods=['PUT'])
def put_user(id):
  data = request.get_json()
  service.update(id, data)
  return jsonify({'id': id}), 200

@user_api.route('/<id>', methods=['DELETE'])
def delete_user(id):
  service.delete(id)
  return jsonify(), 204
