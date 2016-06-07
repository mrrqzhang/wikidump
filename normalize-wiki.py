import sys
import mypythonlib

prev=''
for line in sys.stdin:
    fields = line.strip('\r\t\n').split('\t')
    nword = mypythonlib.normalize_wiki_entity(fields[0])
    if nword and nword != prev: 
        sys.stdout.write('%s\n' % nword)
        prev=nword



