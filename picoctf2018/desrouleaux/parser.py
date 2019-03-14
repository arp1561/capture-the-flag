import json
from pprint import pprint

with open('incidents.json') as f:
	DATA = json.load(f)

data = DATA['tickets']

src_ip = []
dest_ip = []
for i in data:
	src_ip.append(i['src_ip'])
	dest_ip.append(i['dst_ip'])


hashes = []
#print src_ip
for h in data:
	hashes.append(h['file_hash'])
hashes = list(set(hashes))

fdict = {}
for i in hashes:
  fdict[i]=''

for i in hashes:
  s=''
  for j in data:
    if i==j['file_hash']:
      s+=j['dst_ip']+","
  fdict[i]=s


	
pprint(fdict)