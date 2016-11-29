#!/usr/local/python

import urllib2
import sys
import html2text
from bs4 import *

f = open('archivedUrls.txt', 'r')
for line in f:
	url = line.strip()
	if url != '0':
		try:
			print "Requesting at: " + url
			response = urllib2.urlopen(url)
			#parse html
			soup = BeautifulSoup(response.read(), "html.parser")
			filename = './webpages/' + url.replace('/', '') + '.txt'
			fi = open(filename, 'w')
			text = html2text.html2text(soup.prettify())
			text = text.encode('ascii', 'ignore')
			fi.write(text)
			fi.close()
		except:
			print "Error with " + url
f.close()
