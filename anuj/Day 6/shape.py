class shape:
	def __init__(self):
		print "shape"
class rectangle(shape):
	def __init__(self,l,b):
		self.l = l
		self.b = b
		self.__c = self.l+self.b

