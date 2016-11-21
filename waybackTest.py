import requests
import json
import csv

with open('output.csv', 'rb') as cf:
	rdr = csv.reader(cf, delimiter=',')
	for row in rdr:
		print row[6]


"""
z = requests.get("http://archive.org/wayback/available?url=facebook.com")
q = z.json()

print q['archived_snapshots']['closest']['url']

"""