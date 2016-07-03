class timer(object):
	
	#time ( string) - format HHMMSS 
	#repeat (bool) - this is used to repeat every day except the weekend weekend weekend
	#weekend (bool) - this is used to repead in weekend too
	def __init__(self, time, repeat, weekend, message = "", available = True):
		self._time = time
		self._repeat = repeat
		self._weekend = weekend
		self._message = message
		self._available = True

	#getters
	@property
	def time(self):
		return self._time

	@property
	def repeat(self):
		return self._repeat

	@property
	def weekend(self):
		return self._weekend

	@property
	def message(self):
		return self._message

	@property
	def available(self):
		return self._available

	@available.setter
	def available(self, value):
		self.available = value
