from app import db
from users.model import User

class UserRepository:
  def get_all(self):
    return User.query.filter_by(enabled = True).all()

  def get_by_id(self, id):
    return User.query.filter_by(id = id, enabled = True).first()

  def create(self, user):
    db.session.add(user)

    db.session.commit()
    return user

  def update(self, id, user):
    _user = User.query.filter_by(id = id).first()

    _user.username = user['username']
    _user.email = user['email']
    _user.enabled = user['enabled']

    db.session.commit()
    return user

  def delete(self, id):
    _user = User.query.filter_by(id=id).first()

    _user.enabled = False

    db.session.commit()
    return _user
