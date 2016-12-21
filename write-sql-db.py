import sys,re,string

sys.path.append(".")
from utilfunc import *
from datetime import datetime




#schema
#eid, caption, alias, creation_time, creator, suggestion, description


for line in sys.stdin:
  try:
    fields = line.strip('\r\t\n').split('\t')
    if len(fields)<2: continue
    if "(disambiguation)" in fields[0]: continue
    eid = convert_quote(convert_apostrophe(fields[0]))
    wiki_id = eid
    caption = re.sub('_',' ',eid)
    alias = wiki_alias(wiki_id)
    creation_time = str(epochutcnow())   #utcnow() #'1473724679'
    creator = 'wikomega'
    temp = remove_punct(fields[0]).lower()
    temp =  re.split(' ',temp)[0:4]
    suggestion =   '|'.join([ ' '.join(temp[0:i]) for i in range(1,min(4,1+len(temp))) ]) 
    description = '.'.join(re.split('\.',fields[1])[0:2]) + '.'
    description = re.sub("\\\\'\\\\'\\\\'",'',description)  # convert \'\'\' to ''
    description = re.sub("\\\\'\\\\'",'',description)       # convert \'\' to ''
    description = convert_apostrophe(description)          # convert \' to '
    description = convert_quote(description)          # convert \" to "
    description = re.sub('\(.*?\)','',description)
    description = description.split('==')[0]
    sys.stdout.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (eid, wiki_id,caption,alias,creation_time,creator,suggestion,description))
  except: pass
