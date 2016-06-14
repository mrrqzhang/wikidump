import pickle
import gzip
import numpy
import itertools
import sys
from six import iteritems, itervalues, string_types
from gensim.models import Word2Vec
from gensim import utils, matutils

model = Word2Vec.load("en.model")

fname=sys.argv[1]
fout = utils.smart_open(fname, 'w')
#fout.write("storing %sx%s projection weights into %s" % (len(self.vocab), "1000",fname))

fout.write(utils.to_utf8("%s %s\n" % model.syn0.shape))
for word, vocab in sorted(iteritems(model.vocab), key=lambda item: -item[1].count):
    row = model.syn0[vocab.index]
    fout.write(utils.to_utf8("%s %s\n" % (word, ' '.join("%f" % val for val in row))))
