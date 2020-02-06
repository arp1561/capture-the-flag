#!/usr/bin/python3

charMapping={}
for i in range(97,123):
	charMapping[chr(i)]=i-97

def get_key(v):
	for key,val in charMapping.items():
		if v==val:
			return key

def decrypt(cipherText,k):
	plainText=''
	for c in cipherText:
		if c==' ':
			plainText+=' '
		else:
			cipherNum=charMapping[c]
			plainNum=(cipherNum-k)%26
			plainText+=get_key(plainNum)
	return plainText


def main():
	text="ynkooejcpdanqxeykjrubvtagp"
	print("picoCTF{%s}\n" % decrypt(text,22))

if __name__=='__main__':
	main()



    
