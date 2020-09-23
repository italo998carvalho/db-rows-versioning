from users.model import User

def to_object(data):
  username = data['username']
  email = data['email']
  enabled = data['enabled']

  return User(username, email, enabled)

def to_dict_list(data):
  user_list = [None] * len(data)

  for i in range(0, len(data)):
    user = {}
    user['id'] = data[i].id
    user['username'] = data[i].username
    user['email'] = data[i].email
    user['enabled'] = data[i].enabled
    user['created_at'] = data[i].created_at

    user_list[i] = user

  return user_list
