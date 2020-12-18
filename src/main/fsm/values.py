from enum import Enum

class States(Enum):
  ENABLED = 1
  DISABLED = 2

class Events(Enum):
  CREATE = 1
  UPDATE = 2
  DELETE = 3
