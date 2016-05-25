import time

currentTime =  int(time.strftime("%H%M"))
print("Current time : {}".format(currentTime))
if currentTime == 0001:
	print("yes")
else:
	print("no")
