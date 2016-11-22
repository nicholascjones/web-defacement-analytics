## translate.py
import string
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

print wordList


