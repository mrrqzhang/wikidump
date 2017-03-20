# -*- coding: utf-8 -*-


import sys

dir='/'.join(__file__.split('/')[:-1])
if dir=='': dir='.'
sys.path.insert(0,dir+'/mwparserfromhell')

import mwparserfromhell
#import codecs
import re



NChars=1000

#for line in codecs.open(sys.argv[1],"r", "utf-8" ):
for line in sys.stdin:
  try:
    fields = line.strip('\r\t\n').split('\t')
    wikicode = mwparserfromhell.parse(fields[3])
    content = wikicode.strip_code()
#    templates = re.sub(r'thumb.*?\\n','',templates) 
    content = re.sub(r'\{\|.*\|\}','',content)
    content = re.sub(r'\\n','',content)
    image='NA'
    for template in wikicode.filter_templates():
	if 'Infobox' in template.name:
    		 image = template.get('Image').value.strip('\\n\r\n\t ')
		 if image[0:2]=="[[":     # for deep level: [[Image:The rain king x files.jpg|250px|The Rain King|alt=A man is attaches an artificial leg while people watch.]]
			match = re.search(r'\[\[.*:(.*)', image.split('|')[0])
         #               print match
                        if match: image=match.group(1)
                 break ;
    sys.stdout.write('%s\t%s\t%s\n\n' % (fields[2].encode('utf-8'), image,content[0:1000].encode('utf-8')))
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
