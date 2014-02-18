import random
#store random numbers to a file

for i in range(10):
	dirname = "./short"
	filename = dirname+"/test_txt"+str(i)
	f = open(filename,"w")
	for j in range(1000):
		f.write(str(random.randint(0,255))+"\n")	
	f.close()


