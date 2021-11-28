from app.models.base import Base
from constants import db

class Conference(Base):
    __tablename__ = "conference"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)

    def __init__(self, conference_data={}):
        self.title = conference_data.get("title")
        self.description = conference_data.get("description")
        self.start_date = conference_data.get("start_date")
        self.end_date = conference_data.get("end_date")
    
    def native_to_dict(self):
        result = {
        "title": self.title,
        "description": self.description,
        "start_date" :self.start_date.strftime("%Y-%m-%d %H:%M:%S") if self.start_date else None,
        "end_date" : self.end_date.strftime("%Y-%m-%d %H:%M:%S") if self.end_date else None,
        "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S") if self.created_at else None,
        "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%S") if self.updated_at else None
        }
        return result
