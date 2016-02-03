# -*- coding: utf-8 -*-
import sys
import mwparserfromhell
import codecs
import re

#for line in codecs.open(sys.argv[1],"r", "utf-8" ):
for line in sys.stdin:
    fields = line.strip('\r\t\n').split('\t')
#	print(text.encode('utf-8')) #tell python it is utf-8
    wikicode = mwparserfromhell.parse(fields[0])
    sentlist = wikicode.get_tree().split('\n')
#    print "AAAAA",sentlist,"\n"
    leftb=[]
    outstr=''
    for words in sentlist:
        if re.match('^<!--',words): continue
        if words == "{{":
              leftb.append('{{')
              continue
        if words == '}}':
              leftb.pop()
              continue
        if leftb==[]:
              outstr = outstr + ' ' +words ;
	      continue
    print outstr[0:300].encode('utf-8'),"\n"
#	print sec




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
