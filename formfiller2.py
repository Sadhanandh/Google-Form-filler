from lxml.html import fromstring
import random
import string
import sys
import urllib2
import urllib
global_dictn = {}

if len(sys.argv)>1:

	if (sys.argv) >2: 
		num = int(sys.argv[2])
	
	for y in range(num):
		print "This is " + str(y+1) + " try"
		gurl = sys.argv[1]
		cont=urllib2.urlopen(gurl)
		data = cont.read()
		tree = fromstring(data)
		tree.cssselect("form")[0]
		inputtree = tree.cssselect("input")
		radio = [x for x in inputtree if x.attrib["type"]=="radio" or x.attrib["type"]=="checkbox"]
		dictn = {}
		for x in radio:
			val = x.attrib["id"]
			val = val[:val.rfind("_")]
			arr=dictn.get(val,[])
			arr.append(x)
			dictn[val] = arr
		for r in dictn:
			selected = dictn[r][random.randrange(0,len(dictn[r]))]
			global_dictn[selected.attrib["name"]] = selected.attrib["value"]

		text = [x for x in inputtree if x.attrib["type"]=="text"]
		for each in text:
			global_dictn[each.attrib["name"]] = "".join([random.choice(string.lowercase) for i in range(8)])


		textareatree = tree.cssselect("textarea")
		for each in textareatree:
			global_dictn[each.attrib["name"]] = "".join([random.choice(string.lowercase) for i in range(8)])

		selecttree = tree.cssselect("select")
		for each in selecttree:
			valuelist = [ch.attrib["value"] for ch in each.iterchildren()]
			global_dictn[each.attrib["name"]]= valuelist[random.randrange(1,len(valuelist))]

		url = tree.cssselect("form")[0].attrib["action"]
		urllib2.urlopen(url,urllib.urlencode(global_dictn))
