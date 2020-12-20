from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from extensions import db

def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost:15432/db_rows_versioning'

  from users.view import user_api
  app.register_blueprint(user_api, url_prefix = '/user')

  db.init_app(app)

  return app
