from pysnmp.hlapi import *
#from Connection import *
class SNMP:
    
    def __makeQuery(self,OIDlist):
        ObjectTypeMIB = []
        for OID in OIDlist:
            ObjectTypeMIB.append(ObjectType(ObjectIdentity(OID)))
        return ObjectTypeMIB
    
    def sendRequest(self,monitor):
        print("send request ...")
        errorIndication, errorStatus, errorIndex, varBinds = next(
            getCmd(SnmpEngine(), CommunityData(monitor.getCommunity()),
                   UdpTransportTarget((monitor.getIP(), monitor.getPort())),ContextData(),
                  *self.__makeQuery(monitor.getOIDList())
            )
        )
        return errorIndication, errorStatus, errorIndex, varBinds
    
