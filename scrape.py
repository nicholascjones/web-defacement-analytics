#! /usr/bin/python
import csv
import os

from HTMLParser import HTMLParser
class myHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		if tag == 'tr':
			global mybool
			mybool = True
		elif tag == 'td':
			global td 
			td = True
	def handle_endtag(self, tag):
		if tag == 'tr':
			global mybool
			mybool = False


f = open('http:_zone-h.org_archive_page=5.html','r')
parser = myHTMLParser()
mybool = False
mystr = 'START TR\n'
counter = 0
total = []
current = []
important = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
R = False
for line in f.readlines():
	td = False
	parser.feed(line)
	if "href=" in line and "href=\"/mirror" not in line:
		td = True
	if mybool:
		if td:
			counter = counter + 1
			if counter in important:
				if counter is 1: #Time
					offset=0
					print 'Time'
					print line.split('>')[1][:-4]
					current.append(line.split('>')[1][:-4])
				elif counter is 3: #Notifier
					print 'Notifier'
					print line.split('>')[1][:-3]
					current.append(line.split('>')[1][:-3])
				elif counter is 4: #H
					print 'H'
					if "H" in line:
						print 'h'
						current.append("H")
					else:
						print 'no'
						current.append("")
				elif counter is 5: #M
					print 'M'
					if "<td><a" in line:
						print 'm'
						offset+=1
						current.append('M')
					else:
						print 'no'
						current.append("")
	 			elif counter is 6+offset: #R
					print 'R'
					if "<td><a" in line:
						print 'r'
						offset+=1
						current.append("R")
						R = True
					else:
						print 'no'
						current.append('')
				elif counter is 7+offset: #Location
					print 'Location'
					if R:
						current = current[:-1]
					current.append(line.split('"')[-2])
					R = False
				elif counter is 9+offset: #Domain
					print 'Domain'
					current.append(line.split('>')[1][:-1])
				elif counter is 10+offset: #OS
					print 'OS'
					current.append(line.split('>')[1][:-4])
		mystr = mystr + str(counter) + ': ' + line.lstrip()
        if not mybool:
		total.append(current)
		current = []
		counter = 0
		if mystr == 'START TR\n':
			mystr = 'START TR\n'
		else:
			mystr = mystr + 'END TR\n'
			mystr = 'START TR\n'


tf = open("output.csv", "a")
tf.write("Time,Notifier,H,M,R,Country,Domain,OS\n")
print total
for thing in total:
	tf.write("%s,%s,%s,%s,%s,%s,%s,%s\n" % (thing[0],thing[1],thing[2],thing[3],thing[4],thing[5],thing[6],thing[7]))
	for a in thing:
		print a
	print 'end\n'
tf.close()
