class User(object):
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f'Username: {self.username}, Email: {self.email}'
