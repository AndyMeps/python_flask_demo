""" Security definition for the API """
from user import User
from werkzeug.security import safe_str_cmp

USERS = [
    User(1, 'bob', 'asdf')
]

USERNAME_MAPPING = {u.username: u for u in USERS}

USERID_MAPPING = {u.id: u for u in USERS}

def authenticate(username, password):
    """ Auth """
    user = USERNAME_MAPPING.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    """ Identity """
    user_id = payload['identity']
    return USERID_MAPPING.get(user_id, None)
