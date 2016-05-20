
DEFINE TFIDF `python tfidf.py` ship('stopwords.marisa','/tmp/ruiqiang/wikidump/tfidf.py'); ;

%default DocuFreqMin 3  -- minimal document frequency (misspell words)
%default input 'a.1'
%default out  'temp'

data = load '$input' using PigStorage('\t','-noschema') ; ;

entitytable = stream data through TFIDF as (entity:chararray, word:chararray, tf:long) ;
wdf = foreach entitytable generate word ;
wdf = foreach (group wdf by word) generate group as word:chararray, COUNT(wdf) as df:long ;
wdf = filter wdf by df>$DocuFreqMin ;

entitytable = join entitytable by word, wdf by word ;
entitytable = foreach entitytable generate entitytable::entity as entity:chararray, entitytable::word as word:chararray, (double)entitytable::tf/wdf::df as tfidf:double, entitytable::tf as tf:double, wdf::df as df:double ;

entitytable = foreach (group entitytable by entity) {
		tmp = TOP(1000,2,entitytable) ;		
                generate flatten(tmp) as (entity:chararray, word:chararray, tfidf:double, tf:double, df:double) ;  
}

entitytable = group entitytable by entity ;
entitytable = foreach entitytable generate flatten(entitytable) as (entity:chararray, word:chararray, tfidf:double, tf:double, df:double), SUM(entitytable.tfidf) as weight:double ;
entitytable = foreach entitytable generate entity, word, tfidf, tf, df, tfidf/weight as weight:double ;

entitytable = order entitytable by entity, tfidf DESC ;
rmf $out ;

store entitytable into '$out' using PigStorage('\t','-schema')  ;

