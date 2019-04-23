from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///urlstore.db"
db = SQLAlchemy(app)
db.drop_all()
db.create_all()

from urlshortner import routes
