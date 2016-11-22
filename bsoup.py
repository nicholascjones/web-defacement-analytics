#!/usr/local/python

import requests
import sys
#from bs4 import BeautifulSoup

f = open('archivedSites.txt', 'r')
for line in f:
	url = "http://"+line
	print url
	try:
		response = requests.get(url)
		# parse html
		#soup = BeautifulSoup(response.content, "html.parser")
		print "Website: " + line
		#for link in soup.find_all('a'):
			#print link.get('href')
	except:
		print "Unexpected error: ", sys.exc_info()[0]
