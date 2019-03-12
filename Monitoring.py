from SNMP import*
from Monitor import *
import time
import threading

class Monitoring(threading.Thread):
    def __init__(self,device,UPdate,state):
        self.device = device # device to monitoring
        self.protocolSNMP = SNMP()# protocolo de communicacion
        self.upDate = UPdate ## tiempo de actualizacion de los datos
        self.isConected = False # estado de conexion con el dsipositivo a conectar
        self.monitoringUP = state
    def setComunication(self):
        errorIndication,errorStatus, errorIndex,varBinds = self.protocolSNMP.sendRequest(self.device)
        return  errorIndication,errorStatus, errorIndex,varBinds
    def statusConnection(self, errorIndication,errorStatus, errorIndex):
        errorInfo = None
        if errorIndication:
            self.isConected = False
            errorInfo = errorIndication
        elif errorStatus:
            self.isConected = False
            errorInfo = str('%s at %s' % (errorStatus.prettyPrint(),errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            self.isConected = True
        return errorInfo
    def getInfo(self,varBinds):
        info = []
        for varBind in varBinds:
            a,b = (' = '.join([x.prettyPrint() for x in varBind])).split('=')
            info.append(b)
            print(b)
             
        
    def startMonitoring(self):
        errorIndication,errorStatus, errorIndex,varBinds = self.setComunication()
        errorInfo = self.statusConnection(errorIndication,errorStatus, errorIndex)
        if self.isConected:
            self.getInfo(varBinds)
            
    def run(self):
        while self.isUP():
            self.startMonitoring()
            time.sleep(self.getTimeUpDate())
        
    def setTimeUpDate(self,time):
        self.upDate = time
    def getTimeUpDate(self):
        return self.upDate
    def setMonitoringUP(self,e):
        self.monitoringUP = e
    def isUP(self):
        return self.monitoringUP
    
