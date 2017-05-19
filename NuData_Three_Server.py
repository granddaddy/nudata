# code modified from
# https://gist.githubusercontent.com/bradmontgomery/2219997/raw/813c95911b47d255fd21b940e155c7921d290ea2/dummy-web-server.py

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import random

SUCCESS_STATUS = [200]
THROTTLE_SERVER_ERRORS = [500, 502, 503]
CLIENT_ERRORS = [400, 401, 402, 403, 404, \
405, 406, 407, 408, 409, 410, 411, \
412, 413, 414, 415, 416, 417, 418, \
421, 422, 423, 424, 426, 428, 429, \
431, 451]

PERCENTAGE_OF_SERVER_ERROR = 30
PERCENTAGE_OF_CLIENT_ERROR = 30

class S(BaseHTTPRequestHandler):

	def getStatus(self, statuses, index):

		status = statuses[ index % len(statuses) ]

		return status

	def set_headers(self, statuses, r):
		status = self.getStatus(statuses, r)

		self.send_response(status)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def send_server_error(self, r):
		self.set_headers(THROTTLE_SERVER_ERRORS, r)
		self.wfile.write("<html><body><h1>SERVER ERROR</h1></body></html>")

	def send_client_error(self, r):
		self.set_headers(CLIENT_ERRORS, r)
		self.wfile.write("<html><body><h1>CLIENT ERROR</h1></body></html>")

	def send_success(self, r):
		self.set_headers(SUCCESS_STATUS, r)
		self.wfile.write("<html><body><h1>OK</h1></body></html>")

	def do_GET(self):
		r = random.randint(0, 99)

		# simulating errors
		if r < PERCENTAGE_OF_SERVER_ERROR:
			self.send_server_error(r)
		elif r >= PERCENTAGE_OF_SERVER_ERROR and \
		r < PERCENTAGE_OF_SERVER_ERROR + PERCENTAGE_OF_CLIENT_ERROR:
			self.send_client_error(r)
		else:
			self.send_success(r)

def run(server_class=HTTPServer, handler_class=S, port=8080):
	server_address = ('', port)
	httpd = server_class(server_address, handler_class)
	print 'Starting httpd...'
	httpd.serve_forever()

if __name__ == "__main__":
	from sys import argv

	if len(argv) == 2 or len(argv) == 3:
		run(port=int(argv[1]))
		if len(argv) == 3:
			random.seed(int(argv[2]))
	else:
		run()