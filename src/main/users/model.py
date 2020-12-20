from extensions import db
from datetime import datetime
from fsm.values import States

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String, nullable=False)
  email = db.Column(db.String, unique=True, nullable=False)
  client_id = db.Column(db.Integer, nullable=False)
  state = db.Column(db.Enum(States), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False)

  def __init__(self, username, email, client_id, state):
    self.username = username
    self.email = email
    self.client_id = client_id
    self.state = state
    self.created_at = datetime.now()
