from app import db
from datetime import datetime

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String, nullable=False)
  email = db.Column(db.String, unique=True, nullable=False)
  enabled = db.Column(db.Boolean, nullable=False)
  created_at = db.Column(db.DateTime, nullable=False)

  def __init__(self, username, email, enabled):
    self.username = username
    self.email = email
    self.enabled = enabled
    self.created_at = datetime.now()
