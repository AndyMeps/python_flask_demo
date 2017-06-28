""" Item Resource """

import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!")

    @jwt_required()
    def get(self, name):
        try:
            item = ItemModel.find_by_name(name)
        except:
            return {'message': 'An error occurred finding the item'}, 500

        if item:
            return item.json()

        return {'message': 'Item not found'}, 404


    @jwt_required()
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': 'An item with name `{}` already exists.'.format(name)}, 400

        data = Item.parser.parse_args()

        item = ItemModel(name, data['price'])

        try:
            item.save()
        except:
            return {'message': 'An error occurred inserting the item'}, 500

        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete()

        return {'message': 'Item deleted'}

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, data['price'])
        else:
            item.price = data['price']

        item.save()

        return item.json()


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"

        result = cursor.execute(query)

        items = []

        for row in result:
            items.append({'id': row[0], 'name': row[1], 'price': row[2]})

        connection.close()

        return {'items': items}
