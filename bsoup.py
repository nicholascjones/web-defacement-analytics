#!/usr/local/python

import urllib2
import requests
import sys
from bs4 import *

f = open('archivedSites.txt', 'r')
for line in f:
	url = "http://"+line
	print "Requesting at: " + url
	try:
		response = urllib2.urlopen(url)
		#parse html
		#soup = BeautifulSoup(response.read(), "html.parser")
	except:
		print "Unexpected errors: ", sys.exc_info()[0]
