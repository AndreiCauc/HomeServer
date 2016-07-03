from pydoc import locate
import socket
import time
import log

class connection(object):
        def __init__(self, conn, addr, server):
                self._conn = conn
                self._addr = addr
                self._server = server

        def CheckForData(self):
                if self._server.ServerOn == True:
                        log.success("Connection", "Waiting for data from connection")
                        data = self._conn.recv(64)
                        if not data:
                                return
			self._conn.sendall(self.SendAction(data))
			
                       #try:
                       #         input = data.split("/")
                       #         self.SendAction(input[0], input[1])
                       # except:
                       #         log.error("Connection", "Invalid data input")
                self.Close()

        def Close(self):
                self._server.CloseConnection(self)
                self._conn.close()
                log.success("Connection", "Connection is closed!")
                return

        def ForceClosing(self):
                self._conn.close()
                return

        def SendAction(self, data):
		input = data.split("/")
		service_name = ""
		function_name = ""
		args = ""
		try:
			service_name = input[0]
			function_name = input[1]
			if len(input) > 2:
				for i in range(2, len(input)):
					args += "/{}".format(input[i])
		except:
			log.error("Connection", "The input is wrong")

		return self._server.CallService(service_name, function_name, args)
