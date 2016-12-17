DEFINE SUGGESTION `python wiki-suggest.py` ship('/tmp/ruiqiang/wikidump/wiki-suggest.py') ;

%default wikipedia '/projects/qrw/ruiqiang/wiki/entity/' ;
%default wikisuggestion '/projects/qrw/ruiqiang/wiki/suggestion' ;

A = load '$wikipedia' ;


wikiid = foreach A generate $0 as wid:chararray ;

sugg = stream wikiid through SUGGESTION as (wid:chararray,alias:chararray, suggest:chararray) ;

searchlog = load '/projects/qrw/ruiqiang/benzene/*' as (query:chararray, cnt:long) ;
wikicnt = group searchlog by query ;
wikicnt = foreach wikicnt generate group as query:chararray, SUM(searchlog.cnt) as cnt:long ;

suggcnt = foreach ( join sugg by alias, wikicnt by query ) generate
	   sugg::suggest as suggest:chararray, 
	   sugg::wid as wid:chararray,
	   wikicnt::cnt as cnt:long ;

suggrp = foreach ( group suggcnt by suggest ) {
           temp = TOP(20,2,suggcnt) ;
	   generate flatten(temp) ;
}

-- guarrentee  entity has at least one suggestion
alias_sugg = foreach sugg generate alias as suggest:chararray, wid;

alias_sugg = foreach (JOIN alias_sugg by suggest, wikicnt by query) generate
		alias_sugg::suggest as suggest:chararray,
                alias_sugg::wid as wid:chararray,
                wikicnt::cnt as cnt:long ;

merge = union suggrp,alias_sugg ;

merge = foreach (group merge by (suggest,wid) )  {
          temp = TOP(1,2,merge);
          generate flatten(temp) ;
}

wid2sug = foreach (group merge by (wid,cnt)) generate flatten(group) as ( wid:chararray,   cnt:long) , BagToString(merge.suggest, '|')  ;

rmf $wikisuggestion ;

store wid2sug into '$wikisuggestion' ;

