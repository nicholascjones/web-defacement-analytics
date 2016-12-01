## siteParse.py
## get list of words from each parsed site textfile
import string
import os

mList = []


exList = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','wayback','machine','home','page','every','capture','list','captures','url','close','help','see']
exSet = set(exList)


for x,y,z in os.walk("./webpages/"):
	sList = z


for fil in sList:

	lst = []

	fstr = './webpages/' + str(fil)

	f = open(fstr)

	i = 0

	for line in f:
		for w in line.split():
			#print w
			#print w[1:-1]
			if w[1:-1].isalpha():
				#print w
				#print "is alpha!"
				#print w[1:-1]
				if not w[0].isalpha():
					w = w[1:]
				if not w[-1].isalpha():
					w = w[:-1]

				w = w.lower()
				if w not in exSet and len(w) >= 3:
					lst.append(w)

			else:
				pass
				#print "blah"
				#print w[1:-1]
			#print w[1:-2]
			#if isalpha(w[])


	mList.append(lst)


	f.close()


ii = 0
for li in mList:
	print str(ii) + "\n\n\n\n\n\n"
	print li
	ii += 1


