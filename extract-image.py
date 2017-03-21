# -*- coding: utf-8 -*-


import sys

dir='/'.join(__file__.split('/')[:-1])
if dir=='': dir='.'
sys.path.insert(0,dir+'/mwparserfromhell')

import mwparserfromhell
#import codecs
import re



NChars=1000

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
             for item in template.params:
                name = item.name.lower().strip('\r\n\t ')
                value = item.value.strip('\\n\r\n\t ')
		
		if name=='image' or name=='photo' or any( pic in value.lower() for pic in  ['.jpg','.png','.gif' ,'.tiff','.jpeg'] ) :
			image = value
#                 	print image
		        if image[0:2]=="[[":     # for deep level: [[Image:The rain king x files.jpg|250px|The Rain King|alt=A man is attaches an artificial leg while people watch.]]
   			    match = re.search(r'\[\[.*:(.*)', image.split('|')[0])
			    if match: image=match.group(1)
		            break
                
             break 
    sys.stdout.write('%s\t%s\t%s\n\n' % (fields[2].encode('utf-8'), image,content[0:1000].encode('utf-8')))
  except: pass

