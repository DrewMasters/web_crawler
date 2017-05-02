import urllib
import re
import HTMLParser
import Tkinter as tk
import Queue
import operator

visit_links = Queue.Queue()
visited = {}
print("created visit_links and visited")
state = 0
print("created state")

url = "https://docs.python.org/2/library/re.html"
url = "http://google.com"
visit_links.put(url)

def url_visit(url):
	#get domain name of url
	domain = re.search('.+://[\w\.]*',url).group(0)

	print url
	
	#open url
	try: handle = urllib.urlopen(url)
	except:
		return
	html = handle.read()
	
	links = re.findall('"((http|ftp)s?://.*?)"', html)
	count = 0
	for t in links:
		turl = t[0]
		if domain != re.search('.+://[\w\.]*',turl).group(0):
			if turl in visited:
				visited[turl]+=1
			else:
				visited[turl]=1
				visit_links.put(turl)
				count +=1
	print("Found " + str(count) + " remote URLs on " + str(url))

def print_visited():
	sorted_visited = sorted(visited.items(),key=operator.itemgetter(1),reverse=True)
	for i in sorted_visited:
		print(i)

while not visit_links.empty():
	url_visit(visit_links.get())
	print_visited()
