from pydoc import locate
import socket
import time
import log

class connection(object):
        def __init__(self, conn, addr, server):
                self.__conn = conn
                self.__addr = addr
                self.__server = server

        def CheckForData(self):
                if self.__server.ServerOn == True:
                        log.success("Connection", "Waiting for data from connection")
                        data = self.__conn.recv(64)
                        if not data:
                                return
			self.SendAction(data)
                       #try:
                       #         input = data.split("/")
                       #         self.SendAction(input[0], input[1])
                       # except:
                       #         log.error("Connection", "Invalid data input")
                self.Close()

        def Close(self):
                self.__server.CloseConnection(self)
                self.__conn.close()
                log.success("Connection", "Connection is closed!")
                return

        def ForceClosing(self):
                self.__conn.close()
                return

        def SendAction(self, data):
		input = data.split("/")
		service_name = ""
		function_name = ""
		args = ""
		try:
			service_name = input[0]
			function_name = input[1]
			#if len(input) > 2
				
		
		#get service_name
		#get service_function
		#get args
		#call function in serveir - self.__server.CallService(service_name, function_name, args) 
	
#                my_class = locate("{}.service.service".format(service_name))
#                try:
#                        method = getattr(my_class, function_name)
#                        method()
#                except:
#                        log.error("Connection", "There is no service or function with the given input")
