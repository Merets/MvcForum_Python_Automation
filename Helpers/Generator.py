import random

from Helpers.TypeValidator import TypeValidator
from Helpers.User import User


class Generator(object):
    def __init__(self):
        pass

    @classmethod
    def get_random_number(cls, amount_of_digits=6):
        TypeValidator.validate_type(amount_of_digits, int)
        start_num = 10 ** (amount_of_digits - 1)
        end_num = (10 ** amount_of_digits) - 1
        number = random.randint(start_num, end_num)
        return number

    @classmethod
    def generate_user(cls):
        random_number = cls.get_random_number()
        username = "user" + str(random_number)
        password = random_number
        email = username + '@gmail.com'
        new_user = User(username, password, email)
        print(f'New User is generated: {new_user}')
        return new_user
