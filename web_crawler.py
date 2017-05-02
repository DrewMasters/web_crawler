import urllib
import re
import HTMLParser
import Tkinter as tk
import Queue

visit_links = Queue.Queue()

url = "https://docs.python.org/2/library/re.html"
visit_links.put(url)

def url_visit(url):
	#get domain name of url
	domain = re.search('.+://[\w\.]*',url).group(0)
	
	#open url
	handle = urllib.urlopen(url)

	html = handle.read()
	
	links = re.findall('"((http|ftp)s?://.*?)"', html)
	print links[1][0]
	for t in links:
		turl = t[0]
		if domain != re.search('.+://[\w\.]*',turl).group(0):
			print turl

while not visit_links.empty():
	url_visit(visit_links.get())
