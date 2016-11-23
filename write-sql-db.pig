
-- eid, caption, alias, creation_time, creator, suggestion, description

DEFINE DBFORMAT `python write-sql-db.py` ship('/tmp/ruiqiang/wikidump/write-sql-db.py','/homes/ruiqiang/MyPythonLib/mypythonlib.py'); ;

%default input /projects/qrw/ruiqiang/wiki/entity/

data = load '$input' using PigStorage('\t','-noschema') ; ;

entitytable = stream data through DBFORMAT as (eid:chararray,wiki_id:chararray, caption:chararray, alias:chararray, creation_time:chararray, creator:chararray, suggestion:chararray, description:chararray) ;

rmf /projects/qrw/ruiqiang/wikisqldb
store entitytable into '/projects/qrw/ruiqiang/wikisqldb' using PigStorage('\t','-schema') ;

