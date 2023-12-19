from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pathlib


basedir = pathlib.Path(__file__).parent.resolve()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{basedir / 'university.db'}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

