import requests
import json
import csv
from urlparse import urlparse

urlList = []

with open('output.csv', 'rb') as cf:
	rdr = csv.reader(cf, delimiter=',')
	for row in rdr:
		if row[6] != 'Domain':
			p = urlparse(row[6])
			m = p.path.split('/')[0]
			urlList.append(m)

#print urlList

allGood = []
incompleteDomains = []
noArchive = []

for u in urlList:
	
	if u[-3:] == "...":
		#print "flag"
		incompleteDomains.append(u)
	else:
		uStr = "http://archive.org/wayback/available?url=" + u
		#print uStr
		z = requests.get(uStr)
		q = z.json()
		#print q
		if not q['archived_snapshots']:
			noArchive.append(u)
		else:
			allGood.append(u)


print "incomplete domains:"
print len(incompleteDomains)
#print incompleteDomains
for i in incompleteDomains:
	print i
print len(noArchive)
print "\nno archive:"
#print noArchive
for i in noArchive:
	print str(i)
print "\nall good:"
print len(allGood)
#print allGood
for i in allGood:
	print str(i)
	
	
	
