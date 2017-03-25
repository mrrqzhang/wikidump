import sys
import hashlib,urllib
import urllib, urllib2

from httplib import HTTP

import httplib
from urlparse import urlparse
import requests

'''
def checkUrl(url):
    resp = requests.head(url)
#    print url, resp.status_code
    return resp.status_code < 400

'''


def checkUrl(url):
    p = urlparse(url)
    conn = httplib.HTTPSConnection(p.netloc)
    conn.request('HEAD', p.path)
    resp = conn.getresponse()
    return resp.status < 400


'''
def checkUrl(url):
     p = urlparse(url)
     h = HTTP(p[1])
     h.putrequest('HEAD', p[2])
     h.endheaders()
     if h.getreply()[0] == 200: return 1
     else: return 0
'''


for line in sys.stdin:
    fields = line.strip('\r\t\n').split('\t')
    filename=fields[1]
    filename = filename.replace(' ', "_");
    digest = hashlib.md5(filename).hexdigest()
    folder = digest[0] + '/' + digest[0] + digest[1] + '/' + urllib.quote(filename.encode("utf-8")) 
    url1 = 'https://upload.wikimedia.org/wikipedia/commons/' + folder
    url2 = 'https://upload.wikimedia.org/wikipedia/en/' + folder
    if checkUrl(url1):
            sys.stdout.write('%s\t%s\n' % (fields[0],url1))
    else:
        if checkUrl(url2):
            sys.stdout.write('%s\t%s\n' % (fields[0],url2))

