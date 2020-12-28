from enum import Enum

class States(Enum):
  ENABLED = 1
  DISABLED = 2

class Events(Enum):
  UPDATE = 1
  DELETE = 2
