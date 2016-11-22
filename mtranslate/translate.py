## translate.py
import string
import operator
from mtranslate import translate

f = file("t.txt").read()


wordList = []

for word in f.split():
	word = word.lower()
	g = word.translate(None, string.punctuation)
	z = translate(g)
	for w in z.split():
		#print w
		if w.isalpha():
			wordList.append(w.lower())

freq = {}

#print wordList
for word in wordList:
	if word in freq.keys():
		freq[word] += 1
	else:
		freq[word] = 1

print freq

#print sorted(freq.items(), key = )


