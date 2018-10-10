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
class warna:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

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
headers = {'Host': 'ctsearch.entrust.com',
		   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
		   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		   'Accept-Language': 'en-US,en;q=0.5',
		   'Accept-Encoding': 'gzip, deflate',
			   'Referer': 'https://www.entrust.com/ct-search/',
		   'Connection': 'close',
		   'Upgrade-Insecure-Requests': '1',
		   'Content-Length': '0'}
def main():
	domain = str(raw_input("Input Domain: "))
	time.sleep(1)
	print "[+] Loaded : ",domain
	print "[+] Gaining Subdomains..."
	url = 'https://ctsearch.entrust.com/api/v1/certificates?fields=subjectDN&domain={}&includeExpired=true&exactMatch=false&limit=5000'.format(domain)
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
	dataset_list = '\n'.join(domains)
	subdomains = dataset_list.split('\n')
	count = len(subdomains)
	sett = str(count)
	print "[+] Total: " + sett + " Subdomains Gained "
	tanya = str(raw_input("[+] Test the subdomains ?(y/n): "))
	result = []
	if tanya == 'y':
		time.sleep(0.5)
		for i in subdomains:
			try:
				r = requests.get('http://{}'.format(i),timeout=3)
				r.raise_for_status()
				respon = r.status_code
				reason = str(respon)
				if '200' not in reason:
					print warna.FAIL + "http://{}".format(i) + " is DOWN!" + warna.ENDC
				else:
					live = "http://{}".format(i) + "is UP!"
					result.append(live)
					print warna.OKGREEN + "http://{}".format(i) + " is UP!" + warna.ENDC
			except requests.exceptions.ConnectionError:
				print warna.FAIL + "http://{}".format(i) + " is DOWN! " + warna.ENDC
			except requests.exceptions.HTTPError:
				live_error = "http://{}".format(i) + " is UP!"
				result.append(live_error)
				print warna.OKGREEN + "http://{}".format(i) + " is UP!" + warna.ENDC
	
	else:
		print "[+] Okay, Im Exit Baby...."
		sys.exit(2)
	tanya = str(raw_input("[+] Do you want to save this result?(y/n): "))
	time.sleep(0.5)
	if tanya == 'y':
		print warna.WARNING + "Result will be saved as txt files." + warna.ENDC
		nama = raw_input("Input File Name: ")
		formatfile = ".txt"
		print warna.WARNING + "[+] Result will be saved as ",nama+formatfile + warna.ENDC
		for i in result:
			sttr = str(i)
			simpen = open(nama+formatfile, 'a')
			simpen.write('\n'+sttr)
			simpen.close()
		print "[+] Job Done!"
	if tanya == 'n':
		time.sleep(2)
		print warna.OKBLUE + "[+] OK! No Result will be saved,"
		time.sleep(2)
		print "[+] Have a Nice Day, papayyy..."
		sys.exit(3)
main()
