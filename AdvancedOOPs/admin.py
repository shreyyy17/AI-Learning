from user import User
from saveable import Saveable

class Admin(User,Saveable):
    def __init__(self,username,password,access):
        super().__init__(username,password)
        self.access = access

    def __repr__(self):
        return f'<Admin {self.username}, access: {self.access}>'

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'access': self.access,
        }

    # self.save() will be searched in Admin
    # Then in Usr
    # Then in Saveable, where it will be found

    # self.save() uses self.to_dict()

    # self.to_dict() will be searched for in admin, where it will be found