import os

class RPiTrack(object):
	def getCPUtemperature(self):
		res = os.popen('vcgencmd measure_temp').readline()
		temp = (res.replace("temp=","").replace("'C\n",""))
		print("CPU temperature: {}".format(temp))

	def getCPUuse(self):
		usage = (str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip(\
	)))
		print("CPU usage: {}".format(usage))

	# Return RAM information (unit=kb) in a list
	# Index 0: total RAM
	# Index 1: used RAM
	# Index 2: free RAM
	def getRAMinfo(self):
		p = os.popen('free')
		i = 0
		while 1:
			i = i + 1
			line = p.readline()
			if i==2:
				RAM_stats = (line.split()[1:4])
				print("Ram_total - {}\nRam_user - {}\nRam_free - {}".format(round(int(RAM_stats[0]) / 1000,1), round(int(RAM_stats[1]) / 1000,1), round(int(RAM_stats[2]) / 1000,1)))
				return

	# Return information about disk space as a list (unit included)
	# Index 0: total disk space
	# Index 1: used disk space
	# Index 2: remaining disk space
	# Index 3: percentage of disk used
	def getDiskSpace(self):
		p = os.popen("df -h /")
		i = 0
		while 1:
			i = i +1
			line = p.readline()
			if i==2:
				DISK_stats = (line.split()[1:5])
				print("DISK_total - {} \nDISK_FREE - {} \nDISK_perc - {}".format(DISK_stats[0], DISK_stats[1], DISK_stats[3]))
				return
