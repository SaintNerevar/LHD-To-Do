from app.extensions import db
from datetime import datetime

class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer(), primary_key=True)
    description = db.Column(db.String(80), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.date)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def add_task(self, task_desc, user_id):
        task = Task(description=task_desc, user_id=user_id)
        db.session.add(task)
        db.session.commit()

    def __repr__(self):
        return f"<Task: {self.description}"