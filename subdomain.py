# /usr/lib/python
# Kirnath Morscheck
# ZeroByte.ID
import sys
import requests
import urllib3
import re
import json
import time
from termcolor import colored
from pprint import pprint
from colorama import Fore, Back, Style

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings() 

merah = "\033[01;31m{0}\033[00m"
hijau = "\033[01;35m{0}\033[00m"

w 		= merah.format(" _   ___                  _   _     \n")
gans 	= merah.format("| | / (_)                | | | |    \n")
sangat 	= merah.format("| |/ / _ _ __ _ __   __ _| |_| |__  \n")
kirnath = merah.format("|    \| | '__| '_ \ / _` | __| '_ \ \n")
coded 	= merah.format("| |\  \ | |  | | | | (_| | |_| | | |\n")
me 		= merah.format("\_| \_/_|_|  |_| |_|\__,_|\__|_| |_|\n")
exit = "[========]"
for l in w:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.005)
for l in gans:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.005)
for l in sangat:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.005)
for l in coded:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.005)
for l in me:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.005)
print hijau.format("                       ZeroByte.ID\n")

def main():
	domain = str(raw_input("List File: "))
	readfile = open(domain, "r")
	domainsFound = {}
	domainsNotFound = {}
	print("[+] Gaining Domain...")
	time.sleep(1)
	print("[+] Domains Gained...")
	time.sleep(1)
	for data in readfile:
		domains = data.split('\n')
		print "[+] Loaded :",len(domains)
		print "[+] Gaining Subdomains..."
	headers = {'Host': 'ctsearch.entrust.com',
		   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
		   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		   'Accept-Language': 'en-US,en;q=0.5',
		   'Accept-Encoding': 'gzip, deflate',
			   'Referer': 'https://www.entrust.com/ct-search/',
		   'Connection': 'close',
		   'Upgrade-Insecure-Requests': '1',
		   'Content-Length': '0'}

	url = 'https://ctsearch.entrust.com/api/v1/certificates?fields=subjectDN&domain={}&includeExpired=true&exactMatch=false&limit=5000'.format(domains[0])
	response = requests.get(url, headers=headers, verify=False)
	# print response
	domains = []
	restring = re.compile(r"cn\\u003d(.*?)(\"|,)", re.MULTILINE)
	# print restring
	match = re.findall(restring, response.text)
	# print match
	if match:
		for domain in match:
			if((domain[0] not in domains) and not (re.search("^\*\.", domain[0]))):
				domains.append(domain[0])
	dataset_list = '\n [>] '.join(domains)
	print Fore.GREEN,dataset_list

main()
