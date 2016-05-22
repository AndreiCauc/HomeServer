import socket
import threading
import time
from connection import *
import sys
import log

class server(object):
        def __init__(self, PORT):
                self.__PORT = PORT
                self.__ServerOn = False
                self.__connections = []


        @property
        def ServerOn(self):
                return self.__ServerOn

        def StartServer(self):
                self.s = socket.socket()
                self.s.bind(("", self.__PORT))
                self.s.listen(5)
                self.__ServerOn = True
                self.__connections = []
                acc_connections_thread = threading.Thread( target = self.AcceptConnections )
                acc_connections_thread.start()
                log.success("Server", "Server is on")
                return

        def AcceptConnections(self):
                log.success("Server", "Server started accepting connections")
                while self.__ServerOn == True:
                        c, addr = self.s.accept()
                        conn = connection(c, addr, self)
                        new_thread = threading.Thread(target = conn.CheckForData )
                        new_thread.start()
                        self.__connections.append(conn)
                return

        def CloseConnection(self, connection):
                if connection in self.__connections:
                        self.__connections.remove(connection)
                return

        def CloseServer(self):
                for conn in self.__connections:
                        conn.ForceClosing()

                self.__ServerOn = False

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(("127.0.0.1", self.__PORT)) #Find another way
                log.success("Server", "Server is closed.")
                self.s.close()
                return