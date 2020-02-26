from . import db


class SmogMetric(db.Model):
    __tablename__ = "smog_metrics"

    id = db.Column(db.Integer, primary_key=True)
    pm10 = db.Column(db.Float, nullable=False)
    pm25 = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    time = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f"<SmogMetric id={self.id}, time={self.time}>"
