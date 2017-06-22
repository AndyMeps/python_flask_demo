""" User class definition used for authentication """

class User(object):
    """ Used for authentication """
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
