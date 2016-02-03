# -*- coding: utf-8 -*-
import sys
import mwparserfromhell
import codecs
import re

#for line in codecs.open(sys.argv[1],"r", "utf-8" ):
for line in sys.stdin:
    fields = line.strip('\r\t\n').split('\t')
    wikicode = mwparserfromhell.parse(fields[3])
    sec = wikicode.get_tree() #filter_headings() #external_links() #templates() #html_entities()  #headings() #arguments()
    print(sec.encode('utf-8'))
#    for item in sec:
#	print item.encode('utf-8')
#        sys.stdout.write('Name: %s\n' % (item.encode('utf-8')))
#	    print item.params
#	    sys.stdout.write('Param: %s\n' % (item.params.encode('utf-8')))







#	sys.stdout.write('%s\t%s\n' % (fields[2].encode('utf-8'),wikicode.encode('utf-8')))
#	print(wikicode.encode('utf-8'))
#	templates = wikicode.filter_templates()
#	for item in templates:
#	    print(item.encode('utf-8'))
