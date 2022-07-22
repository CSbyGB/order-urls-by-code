#!/usr/bin/python3

import requests
import sys

# We take the list of urls from the argument
urlFile = sys.argv[1]

# Create file to put all our 400 urls
f2 = open("400-codes.txt", "w")
# x = requests.get("https://google.com/")
# print(x.status_code)

with open (urlFile) as f:
	for line in f:
		print(line)
		print("getting: "+line.strip())	
		x = requests.get(line.strip())
		if (x.status_code >= 400) and (x.status_code < 500):
			f2.write("\nurl: "+line+"gives code: "+str(x.status_code))
