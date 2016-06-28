alias python='$HOME/tools/Python-3.4.4/bin/python3'

#create docu freq for all wiki tokens, about 1.7M
#nohup sh dopig.sh wiki-docfreq.pig  
#hadoop fs -cat /projects/qrw/ruiqiang/wiki/docufreq/part* | gunzip | python ../git_mrrqzhang/bbwords/file-to-json.py True > wiki-test-df.json
#../word2vec/feature-binary2asc GoogleNews-vectors-negative300.bin > ../wikidump/GoogleNews-vectors-negative300.score-normalized.txt


if [ 1 -eq 1 ]; then

#get input file url's docfreq'.  NE candidate generation according to wiki entity and long distance match
cat test-sample.1k.txt | python ../git_mrrqzhang/bbwords/article-to-tfidf.py > url-words-df.txt
cat test-sample.1k.txt | python ../git_mrrqzhang/bbwords/dmatch-entity.py | sort | uniq > candidate-entity.txt


#get url's word2vec
hadoop fs -rm url-words-df.txt
hadoop fs -copyFromLocal url-words-df.txt
sh dopig.sh ../git_mrrqzhang/wikidump/wiki-word2vec.pig "-p input=url-words-df.txt -p output=/projects/qrw/ruiqiang/wiki/testsample/url-word2vec"

#get ambiguous entities and wordvec 
hadoop fs -rm candidate-entity.txt
hadoop fs -copyFromLocal candidate-entity.txt
sh dopig.sh ../git_mrrqzhang/wikidump/wiki-norm-intersect.pig "-p input=candidate-entity.txt -p output=/projects/qrw/ruiqiang/wiki/testsample/selectedentities"


sh dopig.sh ../git_mrrqzhang/wikidump/entity-word2vec.pig "-p input=/projects/qrw/ruiqiang/wiki/testsample/selectedentities  -p output=/projects/qrw/ruiqiang/wiki/testsample/entity-word2vec"

fi

#generate json file
if [ 1 -eq 1 ]; then
   hadoop fs -cat /projects/qrw/ruiqiang/wiki/testsample/url-word2vec/part* | gunzip | python ../git_mrrqzhang/bbwords/file-to-json.py True > wiki-test-article.tfidf.json
   hadoop fs -cat /projects/qrw/ruiqiang/wiki/testsample/entity-word2vec/part* | gunzip | python ../git_mrrqzhang/bbwords/file-to-json.py False > wiki-test.tfidf.json
#   cat test-sample.1k.txt | python ../git_mrrqzhang/bbwords/nechunker.new2.py 
fi
