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
    return from_object_to_dict(user)

  def insert(self, data):
    user = from_dict_to_object(data)
    return self.repository.create(user)

  def update(self, id, data):
    user = from_dict_to_object(data)
    return self.repository.update(id, user)

  def delete(self, id):
    return self.repository.delete(id)