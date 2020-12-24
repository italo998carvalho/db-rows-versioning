class StateMachine:
  def __init__(self, state_map):
    self.mapped_states = state_map

  def get_destiny_state(self, origin_state, event):
    state = self.mapped_states.get(origin_state).get(event)
    if not state:
      raise Exception(f"There's no destiny event when the state is {origin_state} and receives an event {event}")

    return state
