import time
from datetime import datetime as dt 


temp_hosts='hosts' #in the current folder (website_blocker)
hosts_path='/etc/hosts'
redirect='127.0.0.1'
webesite_list=['www.facebook.com','facebook.com']

#covert integer today to daytime object
block_start=dt(dt.now().year,dt.now().month,dt.now().day,8)
block_end=dt(dt.now().year,dt.now().month,dt.now().day,12)

def block_website(hosts_file):
	"""
	add banned website to hosts
	"""
	with open(hosts_file,'r+') as file:
		content=file.read()
		for website in webesite_list:
			if website in content:
				pass
			else:
				file.write(redirect + ' ' + website + '\n')
	print('working hours...')

def allow_website(hosts_file):
	"""
	remove banned websites from hosts
	"""
	with open(hosts_file,'r+') as file:
		content=file.readlines()
		file.seek(0)
		for line in content:
			if not any(website in line for website in webesite_list):
				file.write(line)
		file.truncate()
	print('fun hours !')


while True:
	if block_start < dt.now() < block_end:
		block_website(hosts_path)
		
	else:
		allow_website(hosts_path)
	time.sleep(60)
		 






