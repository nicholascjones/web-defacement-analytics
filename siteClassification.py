import os
import string
from urlparse import urlparse

with open("./blacklists/ads/urls")as f:
	uL = f.read().splitlines()

#print uL

urlList = []

for s in uL:
	p = urlparse(s)
	#print s
	#print p
	m = p.path.split('/')[0]
	n = m.replace("ww2.","")
	z = n.replace("www.","")
	#print z
	if z:
		#print p.path
		urlList.append(z)



cats = []

for x,y,z in os.walk("./blacklists"):

	#print x,y,z  ## only want x
	q = x.replace("./blacklists/","")

	#print q
	if q != "./blacklists":
		cats.append(q) #categories


categories = dict((c,None) for c in cats)

#print categories


for key,value in categories.iteritems():
	try:
		fs = "./blacklists/" + str(key) + "/domains"
		with open(fs) as domainList:
			doms = domainList.read().splitlines()
		categories[key] = set(doms)
	except:
		pass

#print categories

#print urlList

urlTest = {}


for u in urlList:
	tmp = {}
	for key,value in categories.iteritems():
		#print key
		try:
			if u in categories[str(key)]:
				tmp[str(key)] = 1
				#print "yes"
			else:
				tmp[str(key)] = 0
				#print "no"
		except:
			pass
	urlTest[u]=tmp

#print urlTest


tf = open("classOutput.csv", "w")

st = "url"
for key,value in categories.iteritems():
	st += ","
	st += str(key)

tf.write(st)


for key,value in urlTest.iteritems():
	q = key
	for k,v in value.iteritems():
		 q += ","
		 q += str(v)
	tf.write(q)
	tf.write("\n")

tf.close()








