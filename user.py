from lift_GUI import user_GUI
from model import *
from lift_GUI import *
class User:
    def __init__(self,name,floor,type, id=None):
        self.id = id
        self.exists = self.getExists()
        self.name, self.floor, self.type= name,floor,type
        self.first_user = first_user(hostname,username,pw,db)
        if self.exists:
            self.name,self.floor,self.type = self.getUser()

    def getExists(self):
        status = read_tbl(hostname,username,pw,db,self.id)
        if not status:
            return False
        else:
            return True

    def getUser(self):
        user = read_tbl(hostname,username,pw,db,self.id)
        return user[0][1],user[0][2],user[0][3]

    def setUser(self):
        try:
            add_user(hostname,username,pw,db, (self.id, self.name, self.floor, self.type))
            user_GUI("User created")
        except:
            user_GUI("unsuccessful")