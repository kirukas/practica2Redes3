import rrdtool
import time

from getSNMP import *

from observiumVol2.CrearLinea import rrdname
from observiumVol2.getSNMP import consultaSNMP

carga_CPU = 0
comunidad = 'comunidadSNMP'

while 1:
    carga_CPU = int(consultaSNMP(comunidad, 'localhost', '1.3.6.1.2.1.25.3.3.1.2.196608'))
    valor = "N:" + str(carga_CPU)
    print(valor)
    ret = rrdtool.update(rrdname, valor)
    rrdtool.dump(rrdname, 'trend.xml')
    time.sleep(1)

if ret:
    print(rrdtool.error())
    time.sleep(300)