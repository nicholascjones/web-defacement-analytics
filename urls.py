#!/usr/bin/python

f = open('output.csv', 'r')
fi = open('urls.txt', 'w')
for line in f.readlines():
	fi.write(line.split(',')[6] + "\n")
f.close()
fi.close()

