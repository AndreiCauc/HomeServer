from timer import *
from timerclass import *

myTimer = timerclass(5)
myTimer.StartTimer()
exit = 0

while exit == 0:
	print("0: Exit")
	print("1: Start timer")
	print("2: Stop timer")
	print("3: Stop alarm")
	print("4: Add timer (HHMM)")
	print("5: Check sound")

	action = raw_input("Select action: ")

	if int(action) == 0:
		myTimer.StopTimer()
		exit = 1
	elif int(action) == 1:
		myTimer.StartTimer()
	elif int(action) == 2:
		myTimer.StopTimer()
	elif int(action) == 3:
		myTimer.StopAlarm()
	elif int(action) == 4:
		tm = raw_input("Time HHMM ")
		mess = raw_input("Message ")
		myTimer.AddTimer(int(tm), False, False, mess)
	elif int(action) == 5:
		myTimer.TestSound()
