import sys
sys.path.append('../../')
import pygame
from timer import *
import threading
import time
from classes import log

class timerclass(object):
	def __init__(self, snooze_time):
		self.__snoozeTime = snooze_time
		self.__timerOn = False
		self.__alarmOn = False
		self.__timers = []
		#pygame.init()
		#self.__music = pygame.mixer.Sound("../../sound.wav")

	def AddTimer(self, tm, repeat, week):
		self.__timers.append(timer(tm, repeat, week))
		return

	def StartTimer(self):
		log.success("Timer", "Starting timer")
		if self.__timerOn == False:
			self.__timerOn = True
			timer_thread = threading.Thread(target = self.CheckForTime)
			timer_thread.start()
			log.info("Timer", "The timer thread is opened")
		else:
			log.warn("Timer", "The timer is allready on")

	def CheckForTime(self):
		while self.__timerOn == True:
			for tmr in self.__timers:
				if int(tmr.time) == int(time.strftime("%H%M")):
					self.StartAlarm()
					if tmr.repeat == False:
						self.__timers.remove(tmr)

			if self.__alarmOn == True:
				log.info("Alarm", "Alarm is on!")
				#if int(pygame.mixer.get_busy()) == 0:
	                                #self.__music.play()
			time.sleep(1)


	def StartAlarm(self):
		if self.__alarmOn == False:
			self.__alarmOn = True
			#if int(pygame.mixer.get_busy()) == 0:
	        	        #self.__music.play()


	def StopAlarm(self):
		if self.__alarmOn == True:
			self.__alarmOn = False
			#if int(pygame.mixer.get_busy()) == 1:
				#self.__music.stop()
			log.info("Timer", "Alarm has stopped")
		return

	def StopTimer(self):
		if self.__timerOn == True:
			self.__timerOn = False
			#if int(pygame.mixer.get_busy()) == 1:
                                #self.__music.stop()
			log.info("Timer", "Timer thread is now closed!")
		
#	def TestSound(self):
		#self.__music.play()
