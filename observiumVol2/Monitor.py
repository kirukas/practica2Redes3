from Connection import *
class Monitor(Connection):
    def __init__(self,ip,port,community,lista):
        Connection.__init__(self,ip,port,community)
        self.listOID = lista
    def inListIOD(self,oid):
        if oid in self.listOID:
            return True
        else :
            return False
    def addIOD(self, oid):
        if self.inListIOD(oid):
            return
        else:
            self.listOID.append(oid)
            return
    def getOIDList(self):
        return self.listOID
    
