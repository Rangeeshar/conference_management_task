"""
ORM model for basic operations
"""
from constants import db
from datetime import datetime

class Base(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    def create(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        db.session.add(self)
        db.session.commit()
    
    def update(self, update_data, filter={}):
        self.updated_at = datetime.now()
        db.session.query(self.__class__).filter_by(**filter).update(update_data)
        db.session.commit() 


    def fetch(self, filters={}):
        results = db.session.query(self.__class__).filter_by(**filters).order_by(self.__class__.created_at).all()
        return [result.native_to_dict() for result in results]