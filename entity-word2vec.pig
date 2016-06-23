register '/homes/ruiqiang/pigudf/udf-pylibs.py' using org.apache.pig.scripting.jython.JythonScriptEngine as myudf;

-- %default input '/projects/qrw/ruiqiang/wiki/toptfidf2' ;
%default input '/projects/qrw/ruiqiang/wiki/temp/article-tfidf.txt' ;

%default output '/projects/qrw/ruiqiang/wiki/article-word2vec' ;

word2vec = load '/projects/qrw/ruiqiang/wiki/GoogleNews-vectors-negative300.score-normalized.txt' as (word:chararray, feature:chararray) ;

wikiwords = load '$input' ;

wikiwords = foreach wikiwords generate (chararray)$0 as wiki:chararray, (chararray)$1 as orig:chararray, (chararray)$2 as uni:chararray, (float)$3 as tfidf:float ;

wordjoin = foreach (join wikiwords by uni, word2vec by word) generate wikiwords::wiki, wikiwords::orig, wikiwords::tfidf, word2vec::feature ;

wordjoin = foreach (group wordjoin by (wiki,orig)) generate flatten(group), myudf.mergedWord2Vec($1) ;

rmf $output ;
store wordjoin into '$output' ;


