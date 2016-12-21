
-- eid, caption, alias, creation_time, creator, suggestion, description

DEFINE DBFORMAT `python write-sql-db.py` ship('/tmp/ruiqiang/wikidump/write-sql-db.py','/tmp/ruiqiang/wikidump/utilfunc.py'); ;

%default input /projects/qrw/ruiqiang/wiki/entity/

%default wikisuggestion '/projects/qrw/ruiqiang/wiki/suggestion' ;

data = load '$input' using PigStorage('\t','-noschema') ; ;

suggest = load '$wikisuggestion' as (wiki_id:chararray, wfreq:long, suggest:chararray) ;

entitytable = stream data through DBFORMAT as (eid:chararray,wiki_id:chararray, caption:chararray, alias:chararray, creation_time:chararray, creator:chararray, suggestion:chararray, description:chararray) ;

entitytable = foreach ( JOIN entitytable by wiki_id, suggest by wiki_id ) generate
                    entitytable::eid, 
                    entitytable::wiki_id,
                    entitytable::caption,
                    entitytable::alias,
                    entitytable::creation_time,
                    entitytable::creator, 
                    suggest::suggest as suggestion:chararray,
                    entitytable::description, 
                    suggest::wfreq as wfreq:long ;

rmf /projects/qrw/ruiqiang/wikisqldb
store entitytable into '/projects/qrw/ruiqiang/wikisqldb' using PigStorage('\t','-schema') ;

