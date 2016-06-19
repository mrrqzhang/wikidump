register '/homes/ruiqiang/pigudf/udf-pylibs.py' using org.apache.pig.scripting.jython.JythonScriptEngine as myudf;

%default output '/projects/qrw/ruiqiang/wiki/word2vec' ;

word2vec = load '/projects/qrw/ruiqiang/wiki/GoogleNews-vectors-negative300.txt' as (word:chararray, feature:chararray) ;

wikiwords = load '/projects/qrw/ruiqiang/wiki/toptfidf2' ;

wikiwords = foreach wikiwords generate (chararray)$0 as wiki:chararray, (chararray)$1 as uni:chararray, (float)$2 as tfidf:float ;

wordjoin = foreach (join wikiwords by uni, word2vec by word) generate wikiwords::wiki, wikiwords::tfidf, word2vec::feature ;

wordjoin = foreach (group wordjoin by wiki) generate group, myudf.mergedWord2Vec($1) ;

rmf $output ;
store wordjoin into '$output' ;


