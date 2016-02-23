wikiroot=/projects/qrw/ruiqiang/wiki
entityroot=$wikiroot/entity
queue=default

hadoop fs -rm -r -skipTrash $entityroot
hadoop jar $HADOOP_PREFIX/share/hadoop/tools/lib/hadoop-streaming.jar \
                -files extract.py \
                -Dfs.permissions.umask-mode=022 \
                -Dmapred.child.java.opts=-Xmx4096m \
                -Dmapreduce.reduce.java.opts=-Xmx4096m \
                -Dmapred.job.queue.name=$queue -Dmapred.job.map.memory.mb=4096 -Dmapreduce.reduce.memory.mb=4096 -Dmapred.child.ulimit=7340032 \
                -Dmapred.output.compress=true -Dmapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec \
                -Dmapreduce.cluster.acls.enabled=false \
                -Dmapreduce.job.acl-view-job=* \
                -Dmapreduce.job.acl-modify-job=* \
                -input  Wikidump/Page.txt \
                -output $entityroot \
                -mapper "cat" \
                -reducer "python extract.py" \
                -jobconf mapred.reduce.tasks=1000 \
                -jobconf mapreduce.task.timeout=0 \
                -cacheArchive 'hdfs://dilithiumblue-nn1.blue.ygrid.yahoo.com/user/ruiqiang/distcachesrc/mwparserfromhell.jar#mwparserfromhell'

