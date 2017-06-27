""" Item model """
import sqlite3


class ItemModel(object):
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def find_by_name(cls, name):
        """ Find an ItemModel in the database """
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name = ?"

        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return cls(*row)

    def json(self):
        """ JSON representation of the ItemModel """
        return {'name': self.name, 'price': self.price}

    def insert(self):
        """ Insert this object in to the database """
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (self.name, self.price))

        connection.commit()
        connection.close()

    def update(self):
        """ Update this object in the database """
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'UPDATE items SET price = ? WHERE name = ?'

        cursor.execute(query, (self.price, self.name))

        connection.commit()
        connection.close()
