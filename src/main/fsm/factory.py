from fsm.state_machine import StateMachine

class StateMachineFactory:
  def __init__(self):
    self.map = {}

  def insert_state_map(self, origin_state, event, destiny_state):
    if origin_state not in self.map.keys():
      self.map[origin_state] = {}

    self.map[origin_state].update({
      event: destiny_state
    })

  def create_fsm(self):
    return StateMachine(self.map)
