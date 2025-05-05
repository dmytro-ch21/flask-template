from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_admin import Admin
from flask_apispec.extension import FlaskApiSpec

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
admin = Admin(name="Admin")
spec = FlaskApiSpec()