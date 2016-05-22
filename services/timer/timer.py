class timer(object):
	def __init__(self, time, repeat, weekend):
		self.__time = time
		self.__repeat = repeat
		self.__weekend = weekend

	@property
	def time(self):
		return self.__time

	@property
	def repeat(self):
		return self.__repeat

	@property
	def weekend(self):
		return self.__weekend
