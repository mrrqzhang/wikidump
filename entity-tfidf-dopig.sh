#use docufreqmin=50 and MaxTokenNumEachEntity=50 output to id3
sh dopig.sh ../git_mrrqzhang/wikidump/entity-tfidf.pig "-Dmapred.cache.archives=hdfs://dilithiumblue-nn1.blue.ygrid.yahoo.com/user/ruiqiang/distcachesrc/mypythonlib.jar#pythonlib -p input=/projects/qrw/ruiqiang/wiki/entity  -p out=/projects/qrw/ruiqiang/wiki/toptfidfid3"
#sh dopig.sh entity-tfidf.pig "-Dmapred.cache.archives=hdfs://dilithiumblue-nn1.blue.ygrid.yahoo.com/user/ruiqiang/distcachesrc/mypythonlib.jar#pythonlib -p input=/projects/qrw/ruiqiang/wiki/entity  -p out=/projects/qrw/ruiqiang/wiki/toptfidf" 
