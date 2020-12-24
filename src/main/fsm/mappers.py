from fsm.values import States

def map_string_to_state(state):
  switcher = {
    'enabled': States.ENABLED,
    'disabled': States.DISABLED
  }

  value = switcher.get(state)
  if value:
    return value
  else:
    raise Exception(f"The state {state} does not exist!")

def map_state_to_string(state):
  switcher = {
    States.ENABLED: 'enabled',
    States.DISABLED: 'disabled'
  }

  value = switcher.get(state)
  if value:
    return value
  else:
    raise Exception(f"The state {state} does not exist!")