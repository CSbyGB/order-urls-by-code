#!/usr/bin/python3

import requests
import sys

# We take the list of urls from the argument
urlFile = sys.argv[1]

# Create file to put all our 400 urls
f400 = open("400-codes.txt", "w")
# x = requests.get("https://google.com/")
# print(x.status_code)

with open (urlFile) as f:
	for line in f:
		print(line)
		print("getting: "+line.strip())	
		# use verify=False with caution
		x = requests.get(line.strip(), verify=False)
		if (x.status_code >= 400) and (x.status_code < 500):
			f400.write("\nurl: "+line+"gives code: "+str(x.status_code))

