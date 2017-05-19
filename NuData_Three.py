# Numerous components on a network, such as DNS servers, switches, load balancers, 
# and others can generate errors anywhere in the life of a given request. 
# The usual technique for dealing with these error responses in a networked environment 
# is to implement retries in the client application. 
# This technique increases the reliability of the application and 
# reduces operational costs for the developer. 
# Write code that implements automatic retry logic and 
# simulates exponential backoff and jitter. 
# For the purposes of this code test, assume that the code you are writing will retry on server or 
# throttling errors but will halt on client errors.

import urllib
import time
import random

SUCCESS_STATUS = [200]
THROTTLE_SERVER_ERRORS = [500, 502, 503]
CLIENT_ERRORS = [400, 401, 402, 403, 404, \
405, 406, 407, 408, 409, 410, 411, \
412, 413, 414, 415, 416, 417, 418, \
421, 422, 423, 424, 426, 428, 429, \
431, 451]

class Three:

	BASE_SLEEP = 1
	EXPONENTIAL_BACKOFF_FACTOR = 2

	# jitter range will be [-n/2, n/2]
	# we enforce jitter_range to be even to
	# make calculation easier
	def __init__(self, jitter_range = 4):

		if jitter_range % 2 != 0:
			raise ValueError("jitter range must be even")

		self.jitter_range = jitter_range

	def getJitter(self):

		return random.randint(0, self.jitter_range) - \
		(self.jitter_range/2)

	def connect(self, host):

		print "Connecting to: " + host + " ..."

		statusCode = 500
		sleepTime = Three.BASE_SLEEP

		while statusCode in THROTTLE_SERVER_ERRORS:

			try:
				conn = urllib.urlopen(host)
			except IOError as e:	
				print "I/O error({0}): {1}".format(e.errno, e.strerror)

				# exponential backoff
				sleepTime = sleepTime * Three.EXPONENTIAL_BACKOFF_FACTOR

				jitter = self.getJitter()

				time.sleep(sleepTime + jitter)

				continue

			statusCode = conn.getcode()
			print statusCode

			# exponential backoff
			sleepTime = sleepTime * Three.EXPONENTIAL_BACKOFF_FACTOR

			jitter = self.getJitter()

			time.sleep(max(sleepTime + jitter, Three.BASE_SLEEP))

		print "=" * 50

		return statusCode


if __name__ == '__main__':
	t = Three()

	while True:
		t.connect("http://127.0.0.1:8080/")