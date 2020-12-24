from users.model import User
from fsm.mappers import *

def from_dict_to_object(data):
  username = data['username']
  email = data['email']
  client_id = data['client_id']
  state = map_string_to_state(data['state'])

  return User(username, email, client_id, state)

def from_object_to_dict(data):
  user = {}
  user['id'] = data.id
  user['username'] = data.username
  user['email'] = data.email
  user['client_id'] = data.client_id
  user['state'] = map_state_to_string(data.state)
  user['created_at'] = data.created_at

  return user

def to_dict_list(data):
  user_list = [None] * len(data)

  for i in range(0, len(data)):
    user = {}
    user['id'] = data[i].id
    user['username'] = data[i].username
    user['email'] = data[i].email
    user['client_id'] = data[i].client_id
    user['state'] = map_state_to_string(data[i].state)
    user['created_at'] = data[i].created_at

    user_list[i] = user

  return user_list
