""" Item model """
from db import db

class StoreModel(db.Model):
    """ Represents a Store in the database """

    # Database Configuration
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # Table References
    items = db.relationship('ItemModel', lazy='dynamic', backref='items')

    # Class Details
    def __init__(self, name):
        self.name = name

    def json(self):
        """ JSON representation of the ItemModel """
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    def save(self):
        """ Upsert this object in to the database """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """ Update this object in the database """
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        """ Find an ItemModel in the database """
        return cls.query.filter_by(name=name).first()
