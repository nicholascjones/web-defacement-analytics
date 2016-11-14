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


f = open('sample.txt','r')
parser = myHTMLParser()
mybool = False
mystr = 'START TR\n'
counter = 0
total = []
current = []
important = [1, 2, 3, 4, 5, 6, 8, 9]
for line in f.readlines():
	td = False
	parser.feed(line)
	if mybool:
		if td:
			counter = counter + 1
			if counter in important:
				if counter is 1:
					current.append(line.lstrip()[4:-7])
				elif counter is 2:
					current.append(line.lstrip()[4:-11].split('>')[-1])
				elif counter is 3 or counter is 4 or counter is 5:
					current.append(line.lstrip()[4:-7])		
				elif counter is 6:
					current.append(line.lstrip()[4:-9].split('"')[-1])
				elif counter is 8:
					current.append(line.lstrip()[4:-2])
				elif counter is 9:
					current.append(line.lstrip()[4:-7])
							
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


tf = open("output.csv", "w")
tf.write("Time,Notifier,H,M,R,Country,URL,OS\n")
print total
for thing in total:
	tf.write("%s,%s,%s,%s,%s,%s,%s,%s\n" % (thing[0],thing[1],thing[2],thing[3],thing[4],thing[5],thing[6],thing[7]))
	#for a in thing:
		#print a
	#print '\n'
tf.close()
