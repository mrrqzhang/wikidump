
A = load '/projects/clickmodel/ckang/usmlr/sim_20150826/query_qvec_out_combined' ;
A = foreach A generate $0 ;

B = load '/projects/qrw/ruiqiang/wikisqldb' ;

C = join A by $0, B by $3 ;

C = foreach C generate $1.. ;

rmf temp ;
store C into 'temp' ;
