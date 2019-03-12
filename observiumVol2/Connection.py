from Device import *

class Connection(Device):
    
    def __init__(self,ip,port,community):
        Device.__init__(self)
        self.IPAdress = ip
        self.Port = port
        self.Community = community
        self.Connected = False
    def setConnection(self,e):
        self.Connected = e
    def isConnected(self):
        return self.Connected
    def setIP(self,ip):
        self.IPAdress = ip
    def setPort(self,port):
        self.Port = port
    def setCommunity(self,c):
        self.Community = c
    def getIP(self):
        return self.IPAdress
    def getPort(self):
        return self.Port
    def getCommunity(self):
        return self.Community
    
    
