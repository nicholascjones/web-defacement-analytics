import requests
import json
import csv
from urlparse import urlparse

urlList = []

with open('outputTest.csv', 'rU') as cf:
	rdr = csv.reader(cf, delimiter= ',')
	for row in rdr:
		#print row
		if row[6] != 'Domain':
			p = urlparse(row[6])
			m = p.path.split('/')[0]
			urlList.append(m)

"""
print urlList
print len(urlList)
"""

for u in urlList:
	#print u
	pass

#print urlList

allGood = []
incompleteDomains = []
noArchive = []

archivedDomains = []

for u in urlList:

	
	if u[-3:] == "...":
		#print "flag"
		incompleteDomains.append(u)
		#print 0
		archivedDomains.append(0)
	else:
		uStr = "http://archive.org/wayback/available?url=" + u
		
		#print uStr
		z = requests.get(uStr)
		q = z.json()
		#print q
		if not q['archived_snapshots']:
			noArchive.append(u)
			archivedDomains.append(0)
			#print 0
		else:
			allGood.append(u)
			archivedDomains.append(uStr)
			#print 1

"""
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
"""
for x in archivedDomains:
	print x
	
	
	
