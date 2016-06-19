import fpg
import interface

class fpg(object):
	"""docstring for fpg"""
	def __init__(self, arg):
		super(fpg, self).__init__()

		self.generator = fpg.Generator();
		self.interface = interface.Server();