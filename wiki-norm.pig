
REGISTER /homes/ruiqiang/pythonlib/myfunc.py USING jython AS pyudf ;

A = load '/projects/qrw/ruiqiang/wiki/toptfidf2/part*' ;
A = foreach A generate pyudf.normalize_wiki_entity($0),$0.. ;
B = load 'test-small-size-ner.txt'  ;
B = foreach B generate $0 as word ;
-- C = cogroup A by $0, B by $0 ;
-- C = filter C by IsEmpty(B) is not null ;
-- C = foreach C generate flatten(A) ;
C = join A by $0, B by $0 ;
C = order C by $0,$1,$2 ;
rmf temp2 ;
store C into 'temp2/C' ;
