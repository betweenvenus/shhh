# All extensions are used as singletons and initialized in application factory.
from flask_apscheduler import APScheduler
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
scheduler = APScheduler()
