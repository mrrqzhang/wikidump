import sys

dir='/'.join(__file__.split('/')[:-1])
if dir=='': dir='.'
sys.path.insert(0,dir+'/pythonlib')
sys.path.insert(0,dir+'/pythonlib/marisa_trie-0.7.2-py2.6-linux-x86_64.egg')

from  mypythonlib import remove_punct
import re

import marisa_trie

markup=['Notes','References','External links','References and external links','Further reading','Notes and references']

stopwordtrie = marisa_trie.Trie()
with open('stopwords.marisa', 'r') as f:
        stopwordtrie.read(f)
     

pattern=re.compile('|'.join(['=\s*'+item+'\s*=' for item in markup]))

wcount=dict()
for line in sys.stdin:
  wcount=dict()
  try:
    entity,defn = line.strip('\r\t\n').split('\t')
    defn = re.split(pattern, defn, re.I)[0]
    defn = re.split(r'<div.*>',defn,re.I)[0]
    words = remove_punct(defn).split()
    print words
#    print words
    for w in words:
        w = w.lower()
        if w.decode('utf-8') in stopwordtrie or w.isdigit(): 
		continue 
        if w in wcount: wcount[w] += 1
        else:
           wcount.setdefault(w,1)
    for key in wcount:
	sys.stdout.write('%s\t%s\t%d\n' % (entity,key,wcount[key]))
  except: pass
