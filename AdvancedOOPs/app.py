from admin import Admin
from database import Database

a = Admin('shrey','1234',3)

a.save()
print(Database.find(lambda x:x['username']=='shrey'))