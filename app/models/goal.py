from flask import current_app
from app import db

class Goal(db.Model):
    goal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)

    def goal_json_object(self):
        return {
            "id": self.goal_id,
            "title": self.title
        }
    def bad_request(self):
        if self.title == None:
            return None 