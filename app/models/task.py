from app.extensions import db
from datetime import datetime

class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer(), primary_key=True)
    description = db.Column(db.String(80), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.date)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<Task: {self.description}"