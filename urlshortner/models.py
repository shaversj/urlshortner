from datetime import datetime
from urlshortner import db


class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shorturl = db.Column(db.String(10))
    url = db.Column(db.String)
    date_created = db.Column(db.Datetime, default=datetime.utcnow)
    num_of_visits = db.Column(db.Integer, autoincrement=True)

    def __repr__(self):
        return f"URL('{self.shorturl}', '{self.url}', '{self.date_created}', '{self.num_of_visits}')"
