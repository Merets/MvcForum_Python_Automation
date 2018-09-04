import random

from Helpers.User import User


class Generator(object):
    def __init__(self):
        pass

    @classmethod
    def get_random_number(cls):
        number = random.randint(100000, 999999)
        return number

    @classmethod
    def generate_user(cls):
        random_number = cls.get_random_number()
        username = "user" + str(random_number)
        password = random_number
        email = username + '@gmail.com'
        new_user = User(username, password, email)
        return new_user
