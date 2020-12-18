from app import db
from datetime import datetime
from fsm.values import States

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String, nullable=False)
  email = db.Column(db.String, unique=True, nullable=False)
  state = db.Column(db.Enum(States), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False)

  def __init__(self, username, email, state):
    self.username = username
    self.email = email
    self.state = state
    self.created_at = datetime.now()
