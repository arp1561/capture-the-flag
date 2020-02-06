#!/usr/bin/python3

file = open("index.html","r")
lines = []
index=0
for line in file:
	if index>=12 and index<=19:
		lines.append(line.lstrip())
	index+=1

lines.sort()
lines.insert(1,lines[-1])
lines=lines[:-1]

flag=[]
for l in lines:
	flag.append(l.split("'")[1])

print(''.join(flag))
	