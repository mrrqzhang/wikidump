import sys,re,string

sys.path.insert(0,'/'.join(__file__.split('/')[:-1]))

#schema
#eid, caption, alias, creation_time, creator, suggestion, description

def remove_punct(sent):
    regex = re.compile(r'([%s])' % re.escape(string.punctuation))
    sent = regex.sub(r' ', sent)
    sent = re.sub('\s+',' ',sent)
    sent = re.sub('\s+$','',sent)
    sent = re.sub('^\s+','',sent)
    return sent


for line in sys.stdin:
  try:
    fields = line.strip('\r\t\n').split('\t')
    if len(fields)<2: continue
    eid = fields[0]
    caption = re.sub('_',' ',eid)
    alias = caption.lower()
    creation_time = '1473724679'
    creator = 'wikomega'
    temp = remove_punct(fields[0]).lower()
    temp =  re.split(' ',temp)[0:4]
    suggestion = '|'.join([ ' '.join(temp[0:i]) for i in range(1,min(4,1+len(temp))) ]) 
    description = '.'.join(re.split('\.',fields[1])[0:2]) + '.'
    sys.stdout.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (eid, caption,alias,creation_time,creator,suggestion,description))
  except: pass
