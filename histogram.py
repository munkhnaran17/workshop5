#!/usr/bin/python3

import sys

total = 0
res = list()
for i in sys.stdin.readlines():
	wordCount = i.split()
	res.append((wordCount[0],int(wordCount[1])))
	total += int(wordCount[1])
	
for w,c in res:
	print(w.ljust(15),"\t[",sep='',end='')
	for i in range(0,c*100//total,5):
		print("*",sep='',end='')
	print("] ",c*100//total,"%",sep='')
