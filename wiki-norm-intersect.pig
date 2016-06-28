
REGISTER /homes/ruiqiang/pythonlib/myfunc.py USING jython AS pyudf ;

%default input1 '/projects/qrw/ruiqiang/wiki/toptfidf2/part*' ;
%default input2 '/projects/qrw/ruiqiang/wiki/toptfidf2/part*' ;
%default output 'temp'

A = load '$input1' ;
A = foreach A generate pyudf.normalize_wiki_entity($0),$0.. ;
B = load '$input2'  ;
B = foreach B generate $0 as word ;
C = join A by $0, B by $0 ;
C = order C by $0,$1,$2 ;
rmf $output ;
store C into '$output' ;
