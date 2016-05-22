class service(object):

	# Initialisation method
	# Create objects and set variables here
	# This will be called when the server starts
	def __init__(self):
		print("Here is the initialisation")

	# This is how a function should look like
	# Args is a array of variables ( "var1" = 3, "var2" = "test" ) #TODO map required variables to sent variables
        def test(self, args):
                print("Default function")


	# This is the close service function 
	# When the server will be closed it will close all it's services in order to close all the opened threads
	# Close all threads in this function if the module have one
	# All services must have this function, don't delete.
	def CloseService(self):
		print("Closing services ")
