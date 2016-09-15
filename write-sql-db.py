import sys,re

from mypythonlib import remove_punct
#schema
#eid, caption, alias, creation_time, creator, suggestion, description
for line in sys.stdin:
    fields = line.strip('\r\t\n').split('\t')
    if len(fields)<2: continue
    eid = fields[0]
    caption = re.sub('_',' ',eid)
    alias = caption.lower()
    creation_time = '1473724679'
    creator = 'wikomega'
    temp = remove_punct(fields[0]).lower()
    suggestion = '|'.join( re.split(' ',temp))
    description = '.'.join(re.split('\.',fields[1])[0:2]) + '.'
    sys.stdout.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (eid, caption,alias,creation_time,creator,suggestion,description))

