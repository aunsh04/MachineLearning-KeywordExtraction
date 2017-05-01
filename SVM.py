import os
import fnmatch
import re
import csv
import string
import math
from collections import Counter

def unique1():
	d1 = {}
	for dirpath, dirs, files in os.walk('SVM_data'):
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
	final1 = []
	d2 = unique1()
	length = len(d2)
	l = []
	for dirpath, dirs, files in os.walk('SVM_data'):
		for filename in fnmatch.filter(files, '*.txt'):
			d3 = {}
			f = open(os.path.join(dirpath, filename))
			for word in f.read().split():
				count = 0
				for i in d2:		
					if word in d2[i]:
						count+=1
				t = d2[filename]
				tfidf = t[word] * math.log(length/count)
				final1.append(tfidf)
	return final1

def unique3():
	l = []
	for dirpath, dirs, files in os.walk('SVM_data'):
		for filename in fnmatch.filter(files, '*.txt'):
			d3 = {}
			f = open(os.path.join(dirpath, filename))
			for word in f.read().split():
				l.append(len(word))
	return l

def unique4():
	d_length = {}
	for dirpath, dirs, files in os.walk('SVM_data'):
		for filename in fnmatch.filter(files, '*.txt'):
			l = []
			f = open(os.path.join(dirpath, filename))
			for word in f.read().split():
				l.append(word)
			d_length[filename] = len(l)
	return d_length
	
def unique5():
	length_dictionary = unique4()
	final_list = []
	for dirpath, dirs, files in os.walk('SVM_data'):
		for filename in fnmatch.filter(files, '*.txt'):
			length = length_dictionary[filename]
			l = {}
			f = open(os.path.join(dirpath, filename))
			c=0
			for word in f.read().split():
				if word in l:
					final_list.append(l[word])
					c+=1
				else:
					if c==0:
						l[word] = 0
						final_list.append(0)	
						c+=1
					else:
						val = c*1.0
						val1 = val/length
						final_list.append(val1)
						l[word] = val1
						c+=1
	return final_list

def unique6():
	final = []
	for dirpath, dirs, files in os.walk('SVM_data'):
		for filename in fnmatch.filter(files, '*.txt'):
			f = open(os.path.join(dirpath, filename))
			l = f.read().split()
			c = 0
			for word in l:
				if c<700: 
					final.append(1)
					c+=1
				else:
					final.append(0)
					c+=1
	return final
	
def unique7():
	final = []
	length_dictionary = unique4()
	for dirpath, dirs, files in os.walk('SVM_data'):
		for filename in fnmatch.filter(files, '*.txt'):
			length = length_dictionary[filename]
			f = open(os.path.join(dirpath, filename))
			l = f.read().split()
			c = 0
			for word in l:
				if c>length-700:
					final.append(1)
					c+=1
				else:
					final.append(0)
					c+=1
	return final

def unique8():
	final = {}
	for dirpath, dirs, files in os.walk('SVM_datacopy'):
		for filename in fnmatch.filter(files, '*.txt'):
			f = open(os.path.join(dirpath, filename))
			l1 = []
			for word in f.read().split():
				l1.append(word)
			final[filename] = l1
	return final	
			

def unique9():
	final = unique8()
	l = []
	for dirpath, dirs, files in os.walk('SVM_data'):
		for filename in fnmatch.filter(files, '*.txt'):
			f = open(os.path.join(dirpath, filename))
			for word in f.read().split():
				if word in final[filename]:
					l.append(1)
				else:
					l.append(0)		
	return l
					
							

	
	
				
first_occurrence = unique5()								
svm_stats = unique2()  
length = unique3()
early = unique6()
end = unique7()
keyword = unique9()
file = open("Workbook1.csv", "w")
file.write("tf-idf,length,position,present_early,present_end,keyword\n") 
for i in xrange(len(svm_stats)):
	file.write(str(svm_stats[i]) + "," + str(length[i]) + "," + str(first_occurrence[i]) + "," + str(early[i]) + "," + str(end[i]) +  "," + str(keyword[i]) + "\n")
file.close()
