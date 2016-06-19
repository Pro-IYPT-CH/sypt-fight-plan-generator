import SimpleHTTPServer
import SocketServer


class Server(object):
	"""docstring for Server"""
	def __init__(self, arg):
		super(Server, self).__init__()
		self.arg = arg
		