#!/usr/bin/python3

import requests
import sys
import urllib3

# Remove warnings when using verify=False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# We take the list of urls from the argument
urlFile = sys.argv[1]

# Create file to put all our 400 urls
f400 = open("400-codes.txt", "w")
# Create file to put all our 200 urls
f200 = open("200-codes.txt", "w")
# Create file to put all our 300 urls
f300 = open("300-codes.txt", "w")
# response = requests.get("https://google.com/")
# print(response.status_code)
ferror = open("error.txt", "w")

with open (urlFile) as f:
	for line in f:
		print(line)
		print("getting: "+line.strip())	
		try:
			# use verify=False with caution
			# Max 20 seconds to connect to server and max 30 seconds to wait on response
			response = requests.get(line.strip(), verify=False, timeout=(20, 30))
			if (response.status_code >= 400) and (response.status_code < 500):
				f400.write("\nurl: "+line.strip()+" gives code: "+str(response.status_code))
			if (response.status_code >= 200) and (response.status_code < 300):
				f200.write("\nurl: "+line.strip()+" gives code: "+str(response.status_code))
			if (response.status_code >= 300) and (response.status_code < 400):
				f300.write("\nurl: "+line.strip()+" gives code: "+str(response.status_code)+" redirects to "+response.geturl())		
		except requests.exceptions.RequestException as error:
			ferror.write("\nurl: "+line.strip()+" Error: "+str(error))
