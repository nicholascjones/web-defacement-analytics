import os
import string


urlList = []

cats = []

for x,y,z in os.walk("./blacklists"):

	#print x,y,z  ## only want x
	cats.append(x)

print cats


