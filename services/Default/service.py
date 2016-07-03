class service(object):

	# Initialisation method
	# Create objects and set variables here
	# This will be called when the server starts
	def __init__(self):
		print("Here is the initialisation")

	# This is how a function should look like
	# Make sure it return a string
        def test(self, arg1, arg2):
                return("Default function - {}, {}".format(arg1, arg2))


	# This is the close service function 
	# When the server will be closed it will close all it's services in order to close all the opened threads
	# Close all threads in this function if the module have one
	# All services must have this function, don't delete.
	def CloseService(self):
		print("Closing services ")
