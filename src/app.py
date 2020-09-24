from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost:15432/db_rows_versioning'
db = SQLAlchemy(app)

from users.view import user_api
app.register_blueprint(user_api, url_prefix = '/user')
