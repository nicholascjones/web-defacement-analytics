import requests
import json
import csv

urlList = []

with open('output.csv', 'rb') as cf:
	rdr = csv.reader(cf, delimiter=',')
	for row in rdr:
		if row[6] != 'Domain':
			urlList.append(row[6])

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
print incompleteDomains
print "\nno archive:"
print noArchive
print "\nall good:"
print allGood
	
	
	
