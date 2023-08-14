from flask import Flask
from databace import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quze.db"

db.init_app(app)
