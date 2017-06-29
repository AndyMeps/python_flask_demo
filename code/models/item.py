""" Item model """
from code.db import db

class ItemModel(db.Model):

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    # Foreign Key on Store
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    @classmethod
    def all(cls):
        """ Return all items """
        return cls.query.all()

    @classmethod
    def find_by_name(cls, name):
        """ Find an ItemModel in the database """
        return cls.query.filter_by(name=name).first()

    def json(self):
        """ JSON representation of the ItemModel """
        return {'id': self.id, 'name': self.name, 'price': self.price}

    def save(self):
        """ Upsert this object in to the database """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """ Update this object in the database """
        db.session.delete(self)
        db.session.commit()
