import os
import fnmatch
import re
import csv
import string
import math
from collections import Counter

def unique1():
	d1 = {}
	for dirpath, dirs, files in os.walk('data'):
		for filename in fnmatch.filter(files, '*.txt'):
			l = []
			f = open(os.path.join(dirpath, filename))
			for word in f.read().split():
				l.append(word)
			d = dict(Counter(l))
			d1[filename]=d
	return d1
            	
def unique2():
	d4 = {}
	d2 = unique1()
	length = len(d2)
	l = []
	for dirpath, dirs, files in os.walk('data'):
		for filename in fnmatch.filter(files, '*.txt'):
			if filename == '53.txt':
				d3 = {}
				f = open(os.path.join(dirpath, filename))
				for word in f.read().split():
					count = 0
					for i in d2:		
						if word in d2[i]:
							count+=1
					t = d2[filename]
					tfidf = t[word] * math.log(length/count)
					d3[t[word]] = tfidf
			else:
				continue
			final1= []
			for i in d3.items():
				final1.append(i)
			d4[filename] = final1
	return d4
