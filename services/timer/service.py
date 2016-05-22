from timerclass import *
class service(object):
	def __init__(self):
		self._timer = timerclass(5)

	def StartTimer(self, args):
                self._timer.StartTimer()

	def StopTimer(self, args):
		self._timer.StopTimer()

	def CloseService(self):
		self.StopTimer()
