from timerclass import *
import types

class service(object):
	def __init__(self):
		print("init")
		self._timer = timerclass(5)

	#Start the timer 
	#Open thread to listen the timer
	def StartTimer(self):
                self._timer.StartTimer()

	#Close the timer
	#Close the timer thread
	def StopTimer(self):
		self._timer.StopTimer()

	#tm (int) - tm is the time in format HHMMSS
	#repeat (bool) - Repeat every day ( except weekend) 
	#week (bool) - Repeat in weekend too
	def AddTimer(self, tm, repeat, week):
		try: 
			self._timer.AddTimer(int(tm), bool(repeat), bool(week))
		except:
			print("Error input")

	#Stop the alarm from "ringing"
	def StopAlarm(self):
		self._timer.StopAlarm()

	#Close the thread ( used when closing the server )
	def CloseService(self):
		print("timer close")
		self.StopTimer()
