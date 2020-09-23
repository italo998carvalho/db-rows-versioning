from app import db
from users.model import User

class UserRepository:
  def get_all(self):
    return User.query.all()

  def get_by_email(self, email):
    return User.query.filter_by(email=email).first()

  def create(self, user):
    db.session.add(user)
    db.session.commit()

    return user

  def update(self, user):
    _user = User.query.filter_by(email=email).first()

    _user.username = user.username
    _user.enabled = user.enabled

    db.session.commit()
    return user

  def delete(self, id):
    _user = User.query.filter_by(id=id).first()

    db.session.delete(_user)
    db.session.commit()

    return _user
