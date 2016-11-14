import os
import string
from urlparse import urlparse

with open("./blacklists/ads/urls")as f:
	uL = f.readlines()



for s in uL:
	p = urlparse(s)
	if p.netloc:
		pass
		#print p.netloc


urlList = []

cats = []

for x,y,z in os.walk("./blacklists"):

	#print x,y,z  ## only want x
	cats.append(x) #categories


categories = dict((c,None) for c in cats)

print categories

"""
for c in cats:
	fs = "./blacklists/" + str(c) + "domains"
	with open(fs) as domainList:
		doms = domainList.readlines()
"""








