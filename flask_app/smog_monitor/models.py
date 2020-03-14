import datetime

from . import db


class SmogMetric(db.Model):
    __tablename__ = "smog_metrics"

    id = db.Column(db.Integer, primary_key=True)
    pm10 = db.Column(db.Float, nullable=False)
    pm25 = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f"<SmogMetric id={self.id}, created={self.created}>"
