class User:
    def __init__(self, id):
        self.id = id
        self.name = self.getName()
        self.floor = self.getFloor()
        self.type = self.getType()

    def getName(self):
        return "Prapti"

    def getFloor(self):
        return self.id

    def getType(self):
        if self.id == 1:
            return "admin"
        else:
            return "user"