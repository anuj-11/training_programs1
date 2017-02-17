class ClassName:
	def __init__(self,a):
		self.a = a
		print "object created"
	def __str__(self):
		return str(self.a)
	def __del__(self):
		print "object removed"
	def sqr(self):
		return self.a**2	
a= ClassName(10);
print a
print a.sqr();
del a
