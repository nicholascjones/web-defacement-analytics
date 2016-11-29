#!/usr/local/python

import urllib2
import sys
import html2text
from bs4 import *

f = open('archivedUrls.txt', 'r')
for line in f:
	url = line
	if line != '0\n':
		try:
			print "Requesting at: " + url
			response = urllib2.urlopen(url)
			#parse html
			soup = BeautifulSoup(response.read(), "html.parser")
			print html2text.html2text(soup.prettify())
		except:
			print "Unexpected errors: ", sys.exc_info()[0]
