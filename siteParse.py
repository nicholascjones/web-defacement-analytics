## siteParse.py
## get list of words from each parsed site textfile

import string

lst = []

f = open('./webpages/http:web.archive.orgweb20150121040201http:mpenvis.nic.in:80.txt')

i = 0

for line in f:
	for w in line.split():
		#print w
		#print w[1:-1]
		if w[1:-1].isalpha():
			print w
			#print "is alpha!"
			#print w[1:-1]
			if not w[0].isalpha():
				w = w[1:]
			if not w[-1].isalpha():
				w = w[:-1]

			w = w.lower()
			#print w.lower()
			lst.append(w)

		else:
			pass
			#print "blah"
			#print w[1:-1]
		#print w[1:-2]
		#if isalpha(w[])


print lst




f.close()

"""
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
"""
