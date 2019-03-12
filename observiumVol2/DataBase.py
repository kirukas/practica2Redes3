import mysql.connector as mariadb
class connectorDB:
    def __init__(self,user,passw,database):
        self.user = user
        self.password = passw
        self.database = database
    def addDevice(self,ip, port,community,nick,syso,contact,location ):

        mariadb_connection = mariadb.connect(user=self.user, password=self.password, database=self.database)
        cursor =  mariadb_connection.cursor()
        try:
            cursor.execute("INSERT INTO device (ip,port,community,nick,opSystem,contact,location) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                           (ip, port,community,nick,syso,contact,location)
            )
        except mariadb.Error as error:
            print("Error: {}".format(error))           
        mariadb_connection.commit()
        #print( "The last inserted id was: ", cursor.lastrowid)
        mariadb_connection.close()
    def getDevices(self):
        mariadb_connection = mariadb.connect(user=self.user, password=self.password, database=self.database)
        cursor = mariadb_connection.cursor()
        #retrieving information
        cursor.execute("SELECT * FROM device")
        for device in cursor:
            print(device)
            #print("device: {}").format(device)
    def deleteDevice(self,ip):
        mariadb_connection = mariadb.connect(user=self.user, password=self.password, database=self.database)
        cursor =  mariadb_connection.cursor()
        try:
            cursor.execute("delete from device  where ip = %s",(ip,) 
            )
        except mariadb.Error as error:
            print("Error: {}".format(error))           
        mariadb_connection.commit()
        mariadb_connection.close()
        
