import unittest
import NuData_Three_Server
from NuData_Three import Three

CLIENT_ERRORS = [400, 401, 402, 403, 404, \
405, 406, 407, 408, 409, 410, 411, \
412, 413, 414, 415, 416, 417, 418, \
421, 422, 423, 424, 426, 428, 429, \
431, 451]

class Test_NuData_Three(unittest.TestCase):

	def test_retryToSuccess(self):
		host = "http://127.0.0.1:8080/"
		t = Three()
		for i in xrange(5):
			statusCode = t.connect(host)
			self.assertTrue(statusCode == 200 or \
				statusCode in CLIENT_ERRORS)

if __name__ == '__main__':
	unittest.main()