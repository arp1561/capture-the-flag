#!/usr/bin/env python
import pwn
import re

host,port = '2018shell.picoctf.com',1225

s = pwn.remote(host,port) 
prompt = s.recv()

print prompt

binary = re.findall('the (.*) as a word',prompt)[0]
answer = hex(int(binary.replace(' ',''),2))[2:].decode('hex')
s.sendline(answer)


prompt = s.recv()
print prompt

hexa = re.findall('the (.*) as a word',prompt)[0]
answer=hexa.decode('hex')
s.sendline(answer)

prompt = s.recv()
print prompt

octal = re.findall('the (.*) as a word',prompt)[0]
#print hex(int(octal.replace(' ',''),8))[2:].decode('hex')
answer=''.join([chr(int(x,8))  for x in octal.split()])
s.sendline(answer)

prompt = s.recv()
print prompt

flag = re.findall('Flag: (.*)',prompt)[0]
print flag
s.close()
