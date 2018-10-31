'''_____________________________________________________________________
|[] R3DXPL0IT SHELL                                            |ROOT]|!"|
|"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""|"| 
|CODED BY > R3DXPLOIT(JIMMY)                                          | |
|EMAIL > RETURN_ROOT@PROTONMAIL.COM                                   | |
|GITHUB > https://github.com/r3dxpl0it                                | |
|WEB-PAGE > https://r3dxpl0it.Github.io                               |_|
|_____________________________________________________________________|/|
'''
import requests 
import bs4 
import argparse

external = []
unknown =  []
fuzzables = []

def extractor(soup , host) : 
	all_links = list()
	for link in soup.find_all('a' , href = True) :
		if link['href'].startswith('/') : 
			if link['href'] not in all_links : 
				all_links.append(host+link['href'])
		elif host in link['href'] : 
			if link['href'] not in all_links : 
				all_links.append( link['href'] )
		elif 'http://' in host : 
			if 'https://'+host.split('http://')[1] in link['href'] and link['href'] not in all_links: 
					all_links.append( link['href'] )
		elif 'http' not in link['href'] and 'www' not in link['href'] and len(link['href']) > 2 and '#' not in  link['href'] : 
			if link['href'] not in all_links : 
				all_links.append(host+'/'+link['href'])
		elif len (link['href']) > 6 : 
			external.append( link['href'] )
		else : 
			unknown.append( link['href'] )
	return all_links
	
	
def fuzzable_extract(linklist):
	fuzzables = []
	for link in linklist : 
		if "=" in link : 
			fuzzables.append(link)
	return fuzzables 	
def xploit(link , host = None) : 
	if host is None : 
		host = link
	res = requests.get(link , allow_redirects=True)
	soup = bs4.BeautifulSoup(res.text , 'lxml')
	return extractor(soup , host)
	
def level2(linklist , host) : 
	final_list = list()
	for link in linklist : 
		for x in xploit(link , host) :
			if x not in final_list : 
					final_list.append(x)
					print("Appended" , x)
		if link not in final_list : 
			final_list.append(link)
	return final_list
	

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='root url', dest='url')
parser.add_argument('-d', '--deepcrawl', help='crawl deaply', dest='deepcrawl', action='store_true')
parser.add_argument('-f', '--fuzzable', help='extract fuzzable', dest='fuzzable', action='store_true')
parser.add_argument('-e', '--external', help='extract external', dest='external', action='store_true')
args = parser.parse_args()

if 'http' not in args.url : 
	args.url = 'http://' + args.url 
if args.deepcrawl : 
	links = level2(xploit(args.url) , args.url)
	if len(links) > 1 : 
		print('\n\n\nLINKS WITH DEEPCRAWL : \n\n\n')
		for link in links : 
			print('>\t' , link)
	else : 
		print ('\n\n\nNo Link Found\n\n\n')
else : 
	links =xploit(args.url)
	if len(links) > 1 : 
		print('\n\n\nLINKS : \n\n\n')
		for link in links : 
			print('>\t' , link)
	else : 
		print ('\n\n\nNo Link Found\n\n\n')
	
if args.fuzzable : 
	if  len(links) > 1 : 
		if len(fuzzable_extract(links)) > 1 : 
			print('\n\n\nFUZZABLE LINKS : \n\n\n')
			for link in fuzzable_extract(links) : 
				print('>\t' , link)
		else : 
			print ('\n\n\nNo Fuzzable Link Found\n\n\n')
			
		
if args.external : 
	if  len(external) > 1 : 
			print('\n\n\nEXTERNAL LINKS : \n\n\n')
			for link in external : 
				print('>\t' , link)
	else : 
			print ('\n\n\nNo EXTERNAL Link Found\n\n\n')
					
		
		
	
		
	
