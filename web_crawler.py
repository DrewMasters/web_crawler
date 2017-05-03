import urllib
import re
import HTMLParser
try:
    #python2
    import Tkinter as tk
except:
    #python3
    import tkinter as tk
import ScrolledText as tkst
import Queue
import operator
import threading

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
        s = "Found " + str(count) + " remote URLs on " + str(url) + "\n"
        T1.insert('insert',s)

def print_visited():
	sorted_visited = sorted(visited.items(),key=operator.itemgetter(1),reverse=True)
	s = ""
	for i in sorted_visited:
		s = s + str(i) +"\n"
	T1.insert('insert',s)

def process():
	global state

	if state ==0:
		url = E1.get()
		visit_links.put(url)
		state = 1
		t = threading.Thread(target=thread_url)
		t.daemon = True
		t.start()
	elif state ==1:
		state = 2
	elif state == 2:
		state =1
	elif state == 3:
		state = 1
                T1.delete(1.0,"end")
		
def thread_url():
	global state
	global visit_links

	while not visit_links.empty():
		if state == 1:
			url_visit(visit_links.get())
		elif state == 2:
			T1.delete(1.0,"end")
			print_visited()
			state =3
	
visit_links = Queue.Queue()
visited = {}
state = 0
top = tk.Tk()
B1 = tk.Button(top, text="start/pause/resume",command=process)
E1 = tk.Entry(top,bd=5)
T1 = tkst.ScrolledText(top)
B1.pack()
E1.pack()
T1.pack()
top.mainloop()
