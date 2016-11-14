#!/usr/local/python

import requests
from bs4 import BeautifulSoup

url = open("http:_zone-h.org_archive.html")
# parse html
soup = BeautifulSoup(url.read(), "html.parser")

print soup.prettify()
