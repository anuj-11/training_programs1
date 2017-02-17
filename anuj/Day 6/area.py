class arear:
	def __init__(self,l,b):
		self.l = l
		self.b = b
	def area(self):
		return self.l*self.b
	def peri(self):
		return 2*(self.l+self.b)
rect= arear(4,2);
print rect.area()
print rect.peri()
