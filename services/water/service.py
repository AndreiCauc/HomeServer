from water import *

class service(object):

	def __init__(self):
		self._water = Water()
		print("\n start water module")

        def StartHydro(self):
		return self._water.StartHydro()

	def StopHydro(self):
		return self._water.StopHydro()

	def GetTemperature(self):
		return self._water.GetTemperature()

	def GetWaterLevel(self):
		return self._water.GetWaterLevel()

	def GetHydroStatus(self):
		return self._water.GetHydroStatus()


	def CloseService(self):
		print("Closing service")
