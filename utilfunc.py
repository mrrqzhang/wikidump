# user defined function for this folder
import sys,re, string,uuid
from datetime import datetime

def epochutcnow():            
#   return int(datetime.utcnow().strftime("%s"))
    return int(unix_time_millis(datetime.utcnow())/1000)

def unix_time_millis(dt):
#    epoch = datetime(1970, 1, 1, 0, 0)  
    epoch = datetime.utcfromtimestamp(0)
    delta = dt-epoch
    return (delta.days*86400+delta.seconds+delta.microseconds/1e6)*1000
#    return (dt - epoch).total_seconds()*1000  #total_seconds() not available for 2.6.6


def utcnow():
    return datetime.utcnow()


def remove_punct(sent):
    regex = re.compile(r'([%s])' % re.escape(string.punctuation))
    sent = regex.sub(r' ', sent)
    sent = re.sub('\s+',' ',sent)
    sent = re.sub('\s+$','',sent)
    sent = re.sub('^\s+','',sent)
    return sent

def suffix_suggestion(word, n=4):
    temp = remove_punct(word).lower()
    ltemp =  re.split(' ',temp)[-n:]
    suggestion = [ ' '.join(ltemp[i:]) for i in range(0, len(ltemp)) ]
    l2temp = [ ltemp[i] for i in range(0,len(ltemp)) if ltemp[i] not in stopwords ]
    suggestion = suggestion +  [ ' '.join(l2temp[0:i]) for i in range(1,min(n,1+len(l2temp))) ]
    return suggestion

def wiki_alias(word):
        return remove_punct(word).lower()



def prefix_suggestion(word,n=4):
    temp = remove_punct(word).lower()
    ltemp =  re.split(' ',temp)[0:n]
    suggestion = [ ' '.join(ltemp[0:i]) for i in range(1,min(n,1+len(ltemp))) ]
    l2temp = [ ltemp[i] for i in range(0,len(ltemp)) if ltemp[i] not in stopwords ]
    suggestion = suggestion +  [ ' '.join(l2temp[0:i]) for i in range(1,min(n,1+len(l2temp))) ]
    return suggestion

def convert_apostrophe(word):
    word = re.sub("\\\\'",'\'',word)
    return word

def convert_quote(word):
    word = re.sub('\\\\"','\"', word)
    return word



