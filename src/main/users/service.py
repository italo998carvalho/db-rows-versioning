from fsm.factory import StateMachineFactory
from fsm.values import *
from users.repository import UserRepository
from users.mappers import *

class UserService:
  def __init__(self):
    self.repository = UserRepository()
    self.state_machine = _start_fsm()

  def get_all(self):
    user_list = self.repository.get_all()
    return to_dict_list(user_list)

  def get_one(self, id):
    user = self.repository.get_by_id(id)
    return from_object_to_dict(user)

  def insert(self, data):
    user = from_dict_to_object(data, States.ENABLED)
    return self.repository.create(user)

  def update(self, id, data):
    next_state = self._get_next_state(id, Events.UPDATE)
    user = from_dict_to_object(data, next_state)
    return self.repository.update(id, user, next_state)

  def delete(self, id):
    next_state = self._get_next_state(id, Events.DELETE)
    return self.repository.change_state(id, next_state)

  def _get_next_state(self, id, event):
    state = self.repository.get_state_by_id(id)
    return self.state_machine.get_destiny_state(state, event)

def _start_fsm():
  sm_factory = StateMachineFactory()
  sm_factory.insert_state_map(States.ENABLED, Events.UPDATE, States.ENABLED)
  sm_factory.insert_state_map(States.ENABLED, Events.DELETE, States.DISABLED)

  return sm_factory.create_fsm()
