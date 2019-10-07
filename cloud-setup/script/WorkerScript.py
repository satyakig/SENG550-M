"""
This script is used to configure the worker nodes.

First Argument: The IP address of yhe master node.

"""
__author__ = "Sajad Sameti"
__maintainer__ = "Sajad Sameti"
__Email__ = "sajad.sameti1@ucalgary.ca"
__status__ = "Final"
__license__ = "GPL"




import subprocess
import sys

masterIP =sys.argv[1]

subprocess.call([ "sudo chown -R ubuntu:ubuntu /usr/local/hadoop"], shell=True)

subprocess.call([ "sudo chmod -R 777 /usr/local/hadoop"], shell=True)

#hadoop-env
subprocess.call(["sed -i 's/${JAVA_HOME}/\/usr/' /usr/local/hadoop/etc/hadoop/hadoop-env.sh"],shell=True)

#core-site
subprocess.Popen([ "sed -i 's/<\/configuration>//' /usr/local/hadoop/etc/hadoop/core-site.xml"], shell=True).wait()

subprocess.Popen([ "sed -i 's/<configuration>//' /usr/local/hadoop/etc/hadoop/core-site.xml"], shell=True).wait()

subprocess.call(["echo '<configuration>' >> /usr/local/hadoop/etc/hadoop/core-site.xml"],shell=True)

subprocess.call([" echo ' <property>' >> /usr/local/hadoop/etc/hadoop/core-site.xml"],shell=True)

subprocess.call([ "echo '  <name>fs.defaultFS</name>' >> /usr/local/hadoop/etc/hadoop/core-site.xml"],shell=True)

subprocess.call([ "echo '  <value>hdfs://{}:9000</value>' >> /usr/local/hadoop/etc/hadoop/core-site.xml".format(masterIP)],shell=True)

subprocess.call([ "echo ' </property>' >> /usr/local/hadoop/etc/hadoop/core-site.xml"],shell=True)

subprocess.call([ "echo '</configuration>' >> /usr/local/hadoop/etc/hadoop/core-site.xml"],shell=True)

#mapred-site
subprocess.call([ "cp /usr/local/hadoop/etc/hadoop/mapred-site.xml.template /usr/local/hadoop/etc/hadoop/mapred-site.xml"],shell=True)

subprocess.call([ " sed -i 's/<\/configuration>//' /usr/local/hadoop/etc/hadoop/mapred-site.xml"],shell=True)

subprocess.call([ "echo ' <property>' >> /usr/local/hadoop/etc/hadoop/mapred-site.xml"],shell=True)

subprocess.call([ "echo '  <name>mapreduce.framework.name</name>' >> /usr/local/hadoop/etc/hadoop/mapred-site.xml"],shell=True)

subprocess.call([ "echo '  <value>yarn</value>' >> /usr/local/hadoop/etc/hadoop/mapred-site.xml".format(masterIP)],shell=True)

subprocess.call([ "echo ' </property>' >> /usr/local/hadoop/etc/hadoop/mapred-site.xml"],shell=True)

subprocess.call([ "echo '</configuration>' >> /usr/local/hadoop/etc/hadoop/mapred-site.xml"],shell=True)

#hdfs-site
subprocess.call(["sed -i 's/<\/configuration>//' /usr/local/hadoop/etc/hadoop/hdfs-site.xml"],shell=True)

subprocess.call([ "echo ' <property>' >> /usr/local/hadoop/etc/hadoop/hdfs-site.xml"], shell=True)

subprocess.call([ "echo '  <name>dfs.replication</name>' >> /usr/local/hadoop/etc/hadoop/hdfs-site.xml"], shell=True)

subprocess.call([" echo '  <value>3</value>' >> /usr/local/hadoop/etc/hadoop/hdfs-site.xml"], shell=True)

subprocess.call([ "echo ' </property>' >> /usr/local/hadoop/etc/hadoop/hdfs-site.xml"], shell=True)

subprocess.call([ "echo ' <property>' >> /usr/local/hadoop/etc/hadoop/hdfs-site.xml"], shell=True)

subprocess.call([ "echo '  <name>dfs.datanode.data.dir</name>' >> /usr/local/hadoop/etc/hadoop/hdfs-site.xml"], shell=True)

subprocess.call([ "echo '  <value>file:///usr/local/hadoop/hadoop_data/hdfs/datanode</value>' >> /usr/local/hadoop/etc/hadoop/hdfs-site.xml"],shell=True)

subprocess.call([" echo ' </property>' >> /usr/local/hadoop/etc/hadoop/hdfs-site.xml"], shell=True)

subprocess.call([ "echo  '</configuration>' >> /usr/local/hadoop/etc/hadoop/hdfs-site.xml"], shell=True)

#yarn-site
subprocess.call(["sed -i 's/<\/configuration>//' /usr/local/hadoop/etc/hadoop/yarn-site.xml"],shell=True)

subprocess.call([ "echo ' <property>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml"], shell=True)

subprocess.call([ "echo '  <name>yarn.nodemanager.aux-services</name>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml"], shell=True)

subprocess.call([" echo '  <value>mapreduce_shuffle</value>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml"], shell=True)

subprocess.call([ "echo ' </property>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml"], shell=True)

subprocess.call([ "echo ' <property>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml"], shell=True)

subprocess.call([ "echo '  <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml"], shell=True)

subprocess.call([ "echo '  <value>org.apache.hadoop.mapred.ShuffleHandler</value>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml"],shell=True)

subprocess.call([" echo ' </property>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml"], shell=True)

subprocess.call([ "echo ' <property>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml"], shell=True)

subprocess.call([ "echo '  <name>yarn.resourcemanager.hostname</name>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml"], shell=True)

subprocess.call([ "echo '  <value>{}</value>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml".format(masterIP)],shell=True)

subprocess.call([" echo ' </property>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml"], shell=True)

subprocess.call([ "echo  '</configuration>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml"], shell=True)



subprocess.call([ "sudo mkdir -p /usr/local/hadoop/hadoop_data/hdfs/datanode"],shell=True)


subprocess.call([ "sudo chown -R ubuntu:ubuntu /usr/local/hadoop"], shell=True)
