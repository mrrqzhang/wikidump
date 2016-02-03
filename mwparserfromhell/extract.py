# -*- coding: utf-8 -*-
import sys
import mwparserfromhell
import codecs
import re

#for line in codecs.open(sys.argv[1],"r", "utf-8" ):
for line in sys.stdin:
  try:
    fields = line.strip('\r\t\n').split('\t')
    wikicode = mwparserfromhell.parse(fields[3])
    templates = wikicode.strip_code()
#    templates = re.sub(r'thumb.*?\\n','',templates) 
    templates = re.sub(r'\{\|.*\|\}','',templates)
    templates = re.sub(r'\\n','',templates)
    sys.stdout.write('%s\t%s\n\n' % (fields[2].encode('utf-8'), templates[0:300].encode('utf-8')))
  except: pass




#    for item in templates:
#           print(item.encode('utf-8'))
#    print wikicode.encode('utf-8'), "\n"
#    print templates.encode('utf-8'),"\n"


#	sec = wikicode.filter_text()
#	print sec
#        for item in sec:
#	    sys.stdout.write('Name: %s\n' % (item.encode('utf-8')))
#	    print item.params
#	    sys.stdout.write('Param: %s\n' % (item.params.encode('utf-8')))
#	for k in range(len(sec)):
#		sys.stdout.write('%d\n%s\n' % (k,sec[k].encode('utf-8')))







#	sys.stdout.write('%s\t%s\n' % (fields[2].encode('utf-8'),wikicode.encode('utf-8')))
#	print(wikicode.encode('utf-8'))
#	templates = wikicode.filter_templates()
#	for item in templates:
#	    print(item.encode('utf-8'))
