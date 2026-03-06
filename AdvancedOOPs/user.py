class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def login(self):
        return 'logged innn'

    def __repr__(self):
        return f'<username: {self.username}, password: {self.password}>'