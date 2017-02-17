class ClassName:
        def __init__(self,a):
                self.a = a
                print "object created"
	def __add__(self,other):
		return self.a+other.a
a= ClassName(10)
other= ClassName(20)
print a+other
		
