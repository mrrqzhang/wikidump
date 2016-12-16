import sys,re,string

#stop words
stopwords=['a','able','about','above','according','accordingly','across','actually','after','afterwards','again','against','all','allow','allows','almost','alone','along','already','also','although','always','am','among','amongst','an','and','another','any','anybody','anyhow','anyone','anything','anyway','anyways','anywhere','apart','appear','appreciate','appropriate','are','around','as','aside','ask','asking','associated','at','available','away','awfully','be','became','because','become','becomes','becoming','been','before','beforehand','behind','being','believe','below','beside','besides','best','better','between','beyond','both','brief','but','by','came','can','cannot','cant','cause','causes','certain','certainly','changes','clearly','co','com','come','comes','concerning','consequently','consider','considering','contain','containing','contains','corresponding','could','course','currently','definitely','described','despite','did','different','do','does','doing','done','down','downwards','during','each','edu','eg','eight','either','else','elsewhere','enough','entirely','especially','et','etc','even','ever','every','everybody','everyone','everything','everywhere','ex','exactly','example','except','far','few','fifth','first','five','followed','following','follows','for','former','formerly','forth','four','from','further','furthermore','get','gets','getting','given','gives','go','goes','going','gone','got','gotten','greetings','had','happens','hardly','has','have','having','he','hello','help','hence','her','here','hereafter','hereby','herein','hereupon','hers','herself','hi','him','himself','his','hither','hopefully','how','howbeit','however','ie','if','ignored','immediate','in','inasmuch','inc','indeed','indicate','indicated','indicates','inner','insofar','instead','into','inward','is','it','its','itself','just','keep','keeps','kept','know','known','knows','last','lately','later','latter','latterly','least','less','lest','let','like','liked','likely','little','look','looking','looks','ltd','mainly','many','may','maybe','me','mean','meanwhile','merely','might','more','moreover','most','mostly','much','must','my','myself','name','namely','nd','near','nearly','necessary','need','needs','neither','never','nevertheless','new','next','nine','no','nobody','non','none','noone','nor','normally','not','nothing','novel','now','nowhere','obviously','of','off','often','oh','ok','okay','old','on','once','one','ones','only','onto','or','other','others','otherwise','ought','our','ours','ourselves','out','outside','over','overall','own','particular','particularly','per','perhaps','placed','please','plus','possible','presumably','probably','provides','que','quite','qv','rather','rd','re','really','reasonably','regarding','regardless','regards','relatively','respectively','right','said','same','saw','say','saying','says','second','secondly','see','seeing','seem','seemed','seeming','seems','seen','self','selves','sensible','sent','serious','seriously','seven','several','shall','she','should','since','six','so','some','somebody','somehow','someone','something','sometime','sometimes','somewhat','somewhere','soon','sorry','specified','specify','specifying','still','sub','such','sup','sure','take','taken','tell','tends','th','than','thank','thanks','thanx','that','thats','the','their','theirs','them','themselves','then','thence','there','thereafter','thereby','therefore','therein','theres','thereupon','these','they','think','third','this','thorough','thoroughly','those','though','three','through','throughout','thru','thus','to','together','too','took','toward','towards','tried','tries','truly','try','trying','twice','two','un','under','unfortunately','unless','unlikely','until','unto','up','upon','us','use','used','useful','uses','using','usually','value','various','very','via','viz','vs','want','wants','was','way','we','welcome','well','went','were','what','whatever','when','whence','whenever','where','whereafter','whereas','whereby','wherein','whereupon','wherever','whether','which','while','whither','who','whoever','whole','whom','whose','why','will','willing','wish','with','within','without','wonder','would','yes','yet','you','your','yours','yourself','yourselves','zero']

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

for line in sys.stdin:
    try:
    	wiki  = convert_apostrophe(convert_quote(line.strip('\r\t\n')))
        suggest1 = set(prefix_suggestion(wiki,100)+suffix_suggestion(wiki,100))
        no_apos = re.sub('\'','',wiki)
        suggest2 = suggest1.union(set(prefix_suggestion(no_apos,100)+suffix_suggestion(no_apos,100)))
	if len(suggest2)==0: continue
	for item in suggest2:
	    sys.stdout.write('%s\t%s\n' % (line.strip('\r\t\n'),item))
    except: pass


