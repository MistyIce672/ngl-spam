import requests
import string, random
from time import sleep
rand1 = random. choice(string. ascii_letters)
rand2 = random. choice(string. ascii_letters)
rand3 = random. choice(string. ascii_letters)
rand4 = random. choice(string. ascii_letters)
with open("txt.txt","r") as f:
	lines = f.readlines()
count = 0
for line in lines:
	rand1 = random. choice(string. ascii_letters)
	rand2 = random. choice(string. ascii_letters)
	rand3 = random. choice(string. ascii_letters)
	rand4 = random. choice(string. ascii_letters)
	count += 1
	url = 'link here'
	myobj = {"question":line,"deviceId":f"b2a007d0-5574-43b6-9e0a-4e3d4dc{rand1}{rand2}{rand3}{rand4}"}
	x = requests.post(url, json = myobj)
	print(f"b2a007d0-5574-43b6-9e0a-4e3d4dc{rand1}{rand2}{rand3}{rand4}")
	print(x)
	print(count)
	sleep(10)

