from Monitoring import *
from Monitor import *
from DataBase import *
from RRDtool import *
from GUI import *
import sys
from PyQt5.QtCore import pyqtSlot

if __name__ == "__main__":
    # app =QtWidgets.QApplication(sys.argv)
    # ex = Ui_MainWindow()
    # ex.show()
    # sys.exit(app.exec_())
    
    IP = '192.168.1.71'
    Port ='161'
    Community = 'SNMPcom'
    nick = 'arch'
    syso = 'linux'
    contact = 'enriqueherme@gmail.com'
    location ='redes 3'
    OIDlist = ['1.3.6.1.2.1.1.1.0','1.3.6.1.2.1.1.6.0','.1.3.6.1.2.1.1.4.0']
    listDevices = []
    user = 'root'
    password = 'terrys'
    database = 'devices'
    timeUPdate = 10 # tiempo de actualizaion en segundos
    n = Monitor(IP,Port,Community,OIDlist)
    listDevices.append(Monitoring(n,timeUPdate,True))
    data  = RDDtool()
    #isCreateRRD, error = data.create('barrame',0,60,1,10)
   # data.inserIn('barrame.rrd',1)
   # data.makeGraph('barrame.rrd','grafica','ejempplo1')
    for device in listDevices:
       device.run()
    #db = connectorDB(user,password,database)
   
    # print("Eliminar datos")
    # db.deleteDevice('192.168.1.69')
    # db.getDevices()
    


    
# Tráfico de interfaz (entrada y salida)
# Estadísticas de paquetes SNMP (entrada y salida)
# Respuestas PING (entrada y salida)
# Respuestas SNMP (entrada y salida)
# Uso del sistema de archivos
