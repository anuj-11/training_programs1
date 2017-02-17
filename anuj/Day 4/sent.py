import sys
fil =sys.argv
def my_txt(fil):
        fr = file(fil[1],'r')
        text = fr.readlines()
        for line in text:
		try:       
			print line
                	words = line.split(" ")
                	print words[1]
		except Exception:
			print "no second word"
my_txt(fil)








           
