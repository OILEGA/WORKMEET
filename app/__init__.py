from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.config.from_object(Config)

# load environment variables .env file
load_dotenv()

# load secret key from environment variable
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

#load database URI from environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#creating a database variable
db = SQLAlchemy(app)

from app.routes.root import *
from app.models.user import *
