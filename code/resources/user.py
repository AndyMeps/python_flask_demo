""" User class definition used for authentication """
import sqlite3
from models.user import UserModel
from flask_restful import Resource, reqparse

class UserRegister(Resource):
    """
    Used for registering new Users
    """

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    def post(self):
        """
        POST endpoint to register a new user at `/register`
        """
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {'message': 'User already exists.'}, 400

        user = UserModel(**data)
        user.save()

        connection.commit()
        connection.close()

        return {'message': 'User created successfully.'}, 201
