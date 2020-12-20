from extensions import db
from users.model import User
from fsm.values import States

class UserRepository:
  def get_all(self):
    return User.query.filter_by(state = States.ENABLED).all()

  def get_by_id(self, id):
    return User.query.filter_by(id = id, state = States.ENABLED).first()

  def create(self, user):
    db.session.add(user)

    db.session.commit()
    return user

  def update(self, id, user):
    _user = User.query.filter_by(id = id).first()

    _user.username = user.username
    _user.email = user.email
    _user.client_id = user.client_id
    _user.state = user.state

    db.session.commit()
    return user

  def delete(self, id):
    _user = User.query.filter_by(id=id).first()

    _user.state = States.DISABLED

    db.session.commit()
    return _user
