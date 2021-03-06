import socket
import threading
import time
from connection import *
import sys
import log

class server(object):
        def __init__(self, PORT, services_array, timeout):
                self._PORT = PORT
                self._ServerOn = False
                self._connections = []
		self._services = {}
		self._services_array = services_array
		self._timeout = timeout

        @property
        def ServerOn(self):
                return self._ServerOn

	@property
	def Services(self):
		return self._services

	def CallService(self, service_name, service_function, args):
		if args != "":
			args = args[1:]
		if ( not service_name in self._services ):
			log.error("Server", "The service name is incorrect.")
			return
		try:
			method = getattr(self._services[service_name], service_function)
			args = args.split("/")

			if args[0] != "":
				res = method(*args)
				log.info("Recieved", res)
				return res
			else:
				res = method()
				log.info("Recieved", res)
				return res
		except:
			log.error("Server", "Function name is incorrect.")
				 
		#check if self._services contains the service
		#if not, check for service in services folder
		#check for function
		#call the function

        def StartServer(self):
                self.s = socket.socket()
                self.s.bind(("", self._PORT))
                self.s.listen(5)
		#self.s.settimeout(self._timeout)
                self._ServerOn = True
                self._connections = []
                acc_connections_thread = threading.Thread( target = self.AcceptConnections )
                acc_connections_thread.start()

		#initializing services
		log.success("Server", "Initalizing services")
		for string in self._services_array:
                        self._services[string] = __import__("{}.service".format(string)).service.service()
		
                log.success("Server", "Server is on")
                return

        def AcceptConnections(self):
                log.success("Server", "Server started accepting connections")
                while self._ServerOn == True:
                        c, addr = self.s.accept()
			log.info("New connection", "We have a new connection!!")
			c.settimeout(self._timeout)
                        conn = connection(c, addr, self)
                        new_thread = threading.Thread(target = conn.CheckForData )
                        new_thread.start()
                        self._connections.append(conn)
                return

        def CloseConnection(self, connection):
                if connection in self._connections:
                        self._connections.remove(connection)
                return

        def CloseServer(self):
                for conn in self._connections:
                        conn.ForceClosing()

                self._ServerOn = False

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(("127.0.0.1", self._PORT)) #Find another way
		#close all services
		for sr in self._services:
			self._services[sr].CloseService()

                log.success("Server", "Server is closed.")
                self.s.close()
                return
