%default output '/projects/qrw/ruiqiang/wiki/docufreq' ;

%default input '/projects/qrw/ruiqiang/wiki/toptfidf2'

wikiwords = load '$input' ;

wikiwords = foreach wikiwords generate  (chararray)$1 as uni:chararray, (long)$4 as df:long ;

wikiwords = distinct wikiwords ;

wikiwords = order wikiwords by $0 ;

rmf $output ;
store wikiwords into '$output' ;


