class timer(object):
	
	#time ( string) - format HHMMSS 
	#repeat (bool) - this is used to repeat every day except the weekend weekend weekend
	#weekend (bool) - this is used to repead in weekend too
	def __init__(self, time, repeat, weekend):
		self.__time = time
		self.__repeat = repeat
		self.__weekend = weekend

	#getters
	@property
	def time(self):
		return self.__time

	@property
	def repeat(self):
		return self.__repeat

	@property
	def weekend(self):
		return self.__weekend
