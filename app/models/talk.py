from app.models.base import Base
from constants import db


class Talk(Base):
    __tablename__ = "talk"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    duration = db.Column(db.DateTime)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    speakers = db.Column(db.ARRAY(db.String()))
    participants = db.Column(db.ARRAY(db.String()))

    def __init__(self, talk_data):
        self.title = talk_data.get("title")
        self.description = talk_data.get("description")
        self.duration = talk_data.get("duration")
        self.start_time = talk_data.get("start_time")
        self.end_time = talk_data.get("end_time")
        self.speakers = talk_data.get("speakers", [])
        self.participants = talk_data.get("participants", [])

    def native_to_dict(self):
        result = {
            "title": self.title,
            "description": self.description,
            "duration": self.duration,
            "start_time": self.start_time.strftime("%Y-%m-%d %H:%M:%S") if self.start_time else None,
            "end_time": self.end_time.strftime("%Y-%m-%d %H:%M:%S") if self.end_time else None,
            "speakers": self.speakers,
            "participants": self.participants,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S") if self.created_at else None,
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S") if self.updated_at else None,
        }
        return result
