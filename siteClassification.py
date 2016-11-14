import os
import string
from urlparse import urlparse

with open("./blacklists/ads/urls")as f:
	uL = f.readlines()


print uL

uL = set(uL)

for s in uL:
	p = urlparse(s)
	if p.netloc:
		print p.netloc
	else:
		print "~~~~~~~~\n~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~"


urlList = []

cats = []

for x,y,z in os.walk("./blacklists"):

	#print x,y,z  ## only want x
	cats.append(x)

print cats



