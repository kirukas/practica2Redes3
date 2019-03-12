class Device:
    def __init__(self):
        self.nick  = None
        self.syso = None
        self.contact = None
        self.location = None
    def setNick(self,n ):
        self.nick = n
    def setOperativeSystem(self,syso):
        self.syso = syso
    def setContac(self, c):
        self.contact = c
    def setLocation(self,l):
        self.location = l
    def getNick(self):
        return self.nick
    def getOperativeSystem(self):
        return self.syso
    def getContact(self):
        return self.contact
    def getLocation(self):
        return self.location
    
