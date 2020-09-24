from users.repository import UserRepository
from users.mappers import *

class UserService:
  def __init__(self):
    self.repository = UserRepository()

  def get_all(self):
    user_list = self.repository.get_all()
    return to_dict_list(user_list)

  def get_one(self, id):
    user = self.repository.get_by_id(id)
    return to_dict(user)

  def insert(self, data):
    user = to_object(data)
    return self.repository.create(user)

  def update(self, id, data):
    user = to_object(data)
    return self.repository.update(id, data)

  def delete(self, id):
    return self.repository.delete(id)