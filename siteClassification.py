import os
import string
from urlparse import urlparse

with open("./blacklists/ads/urls")as f:
	uL = f.readlines()

urlList = []


for s in uL:
	p = urlparse(s)
	if p.netloc:
		urlList.append(p.netloc)



cats = []

for x,y,z in os.walk("./blacklists"):

	print x,y,z  ## only want x
	q = x.replace("./blacklists/","")
	#print q
	cats.append(q) #categories


categories = dict((c,None) for c in cats)

print categories


for key,value in categories.iteritems():
	try:
		fs = "./blacklists/" + str(key) + "/domains"
		with open(fs) as domainList:
			doms = domainList.read().splitlines()
		categories[key] = set(doms)
	except:
		pass

urlTest = {}








