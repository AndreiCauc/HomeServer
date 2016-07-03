import smbus
import time

class Water(object):

	#Water module
	# -- Mapping --
	#1. Start Module
	#2. Stop Module
	#3. Check temperature
	#4. Check water level
	#5. Check Hydro Status

	def __init__(self):
 		self._bus = smbus.SMBus(1)
		self._address = 0x04
		self._sleepDelay = 0.1
		
	def StartHydro(self):
		self.SendNumber(1)
		time.sleep(self._sleepDelay)
		res = self.ReadNumber()
		return str(res)

	def StopHydro(self):
		self.SendNumber(2)
		time.sleep(self._sleepDelay)
		res = self.ReadNumber()
		return str(res)

	def GetWaterLevel(self):
		self.SendNumber(4)
		time.sleep(self._sleepDelay)
		return self.ReadNumber()

	def GetTemperature(self):
		self.SendNumber(3)
		time.sleep(self._sleepDelay)
		return self.ReadNumber()

	def GetHydroStatus(self):
		self.SendNumber(5)
		time.sleep(self._sleepDelay)
		return str(self.ReadNumber())

	def SendNumber(self, number):
		self._bus.write_byte(self._address, number)

	def ReadNumber(self):
		return str(self._bus.read_byte(self._address))
