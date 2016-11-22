#!/usr/local/python

import requests
import sys
from bs4 import *

f = open('archivedUrls.txt', 'r')
for line in f:
	url = line
	if line == '0\n':
		continue
	else:
		try:
			print "Requesting at: " + url
			response = requests.get(url)
			#parse html
			soup = BeautifulSoup(response.content, "html.parser")
			print soup.prettify()
		except:
			print "Unexpected errors: ", sys.exc_info()[0]
