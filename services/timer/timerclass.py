import sys
sys.path.append('../../')
import pygame
from timer import *
import threading
import time
from classes import log

class timerclass(object):
	def __init__(self, snooze_time):
		self._snoozeTime = snooze_time
		self._timerOn = False
		self._alarmOn = False
		self._timers = []
		#pygame.init()
		#self._music = pygame.mixer.Sound("../../sound.wav")

	def AddTimer(self, tm, repeat, week):
		self._timers.append(timer(tm, repeat, week))
		log.info("Timer", "Timer has beed added")
		return

	def StartTimer(self):
		log.success("Timer", "Starting timer")
		if self._timerOn == False:
			self._timerOn = True
			timer_thread = threading.Thread(target = self.CheckForTime)
			timer_thread.start()
			log.info("Timer", "The timer thread is opened")
		else:
			log.warn("Timer", "The timer is allready on")

	def CheckForTime(self):
		while self._timerOn == True:
			for tmr in self._timers:
				log.info("Timer", "check {} - {} ".format(tmr.time, time.strftime("%H%M")))
				if tmr.time == int(time.strftime("%H%M")):
					self.StartAlarm()
					if tmr.repeat == False:
						self._timers.remove(tmr)

			if self._alarmOn == True:
				log.info("Alarm", "Alarm is on!")
				#if int(pygame.mixer.get_busy()) == 0:
	                                #self._music.play()
			time.sleep(1)


	def StartAlarm(self):
		if self._alarmOn == False:
			self._alarmOn = True
			#if int(pygame.mixer.get_busy()) == 0:
	        	        #self._music.play()


	def StopAlarm(self):
		if self._alarmOn == True:
			self._alarmOn = False
			#if int(pygame.mixer.get_busy()) == 1:
				#self._music.stop()
			log.info("Timer", "Alarm has stopped")
		return

	def StopTimer(self):
		if self._timerOn == True:
			self._timerOn = False
			#if int(pygame.mixer.get_busy()) == 1:
                                #self._music.stop()
			log.info("Timer", "Timer thread is now closed!")
		
#	def TestSound(self):
		#self._music.play()
