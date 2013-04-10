import urllib
import urllib2
import sys
import re
import random 
import string
num = 1
gurl = ""
if len(sys.argv)>1:

	if (sys.argv) >2: 
		num = int(sys.argv[2])

	for y in range(num):
		gurl = sys.argv[1]
		cont=urllib2.urlopen(gurl)
		data = cont.read()
		tups=re.findall("(entry\.\d*)",data,re.I)
		url = gurl[:gurl.rfind("/")] + "/formResponse"
		data = {}
		for x in tups:
			data[x] = "".join([random.choice(string.lowercase) for i in range(8)])
		urllib2.urlopen(url,urllib.urlencode(data))
