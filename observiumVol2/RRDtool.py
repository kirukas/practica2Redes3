import rrdtool
import time 
class RDDtool:
           
    def __typesDB(self,t):
        type =['COUNTER','GAUGE','DERIVE','ABSOLUTE']
        return type[t]
    def create(self,name,typeVar,timeUpdate,sampleAverage,sampleTotal):
        vmax = 'U'
        vmin = 'U'
        typeVariable = self.__typesDB(typeVar)
        nameDB = str(name+'.rrd')
        ErrorInfo = rrdtool.create(
            nameDB,#nombre de la base 
            "--start",'N',# tiempo de inicio de la base 
            "--step",str(timeUpdate),#tiempo en segundos, en que recibe acutualizacion  muestras 
            str('DS:'+name+':'+typeVariable+':'+
                str(timeUpdate)+':'+str(vmin)+':'+str(vmax)),
            str("RRA:AVERAGE:0.5:"+str(sampleAverage)+':'+str(sampleAverage))
        )
        if ErrorInfo:
            return False,ErrorInfo
        else:
            return True,nameDB

    def inserIn(self, nameDB, value):
        rrdtool.update(
            nameDB, str(str(int( time.time()))+':'+str(value))
        )
    def dump(self, nameDB,toFile):
        rrdtool.dump(nameDB,toFile)
    def makeGraph(self,nameDB,nameGraph,title):
        rrdtool.graph(
            str(nameGraph+".png"),
            "--start",str(rrdtool.first(nameDB)),
            "--end",str(rrdtool.last(nameDB)),
            str("DEF:"+nameGraph+"="+nameDB+":"+'barrame'+':AVERAGE'),
            str("LINE1:"+nameGraph+"#ff0000")
        )
        
        
# *COUNTER -> siempre se incrementa, intervalo de tiempo
#  ejem trafico de red,bytes/s
# *GAUGE
#  indicador, distintos valores en el tiempo
#  registra el valor "tal como lo medimos" Ej. uso de cpu, número de usuarios,temperatura
# *DERIVE contador, puede decrecer
# * ABSOLUTE ->valor absoluto
#  contador que se resetea tras su lectura
#  registra el valor, el incremento es implícito
