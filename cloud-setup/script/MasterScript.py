"""
This script is used to configure hadoop on the master node of the hadoop cluster.
The inputs to this script is:
First Argument : worker nodes in the following fashion "<WorkerHostName1>;<WorkerHostName2>;<WorkerHostName3>" for example : "HW1;HW2;HW3"
Second Argument : IP address of the master nodes.


"""
__author__ = "Sajad Sameti"
__maintainer__ = "Sajad Sameti"
__Email__ = "sajad.sameti1@ucalgary.ca"
__status__ = "Final"
__license__ = "GPL"



import subprocess
import sys
workerString = sys.argv[1]

workerNodes = workerString.split(",")

masterIP = sys.argv[2]

masterNode = sys.argv[3]

subprocess.call(['sudo chown -R ubuntu:ubuntu /usr/local/hadoop '], shell=True)
subprocess.call(["sudo chmod -R 777 /usr/local/hadoop"], shell=True)

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

subprocess.call(["echo ' <property>' >> /usr/local/hadoop/etc/hadoop/hdfs-site.xml"], shell=True)

subprocess.call(["echo '  <name>dfs.replication</name>' >> /usr/local/hadoop/etc/hadoop/hdfs-site.xml"], shell=True)

subprocess.call(["echo '  <value>3</value>' >> /usr/local/hadoop/etc/hadoop/hdfs-site.xml"], shell=True)

subprocess.call(["echo ' </property>' >> /usr/local/hadoop/etc/hadoop/hdfs-site.xml"], shell=True)

subprocess.call(["echo ' <property>' >> /usr/local/hadoop/etc/hadoop/hdfs-site.xml"], shell=True)

subprocess.call(["echo '  <name>dfs.namenode.name.dir</name>' >> /usr/local/hadoop/etc/hadoop/hdfs-site.xml"], shell=True)

subprocess.call(["echo '  <value>file:///usr/local/hadoop/hadoop_data/hdfs/namenode</value>' >> /usr/local/hadoop/etc/hadoop/hdfs-site.xml"], shell=True)

subprocess.call(["echo ' </property>' >> /usr/local/hadoop/etc/hadoop/hdfs-site.xml"], shell=True)

subprocess.call(["echo '</configuration>' >> /usr/local/hadoop/etc/hadoop/hdfs-site.xml"], shell=True)

#yarn-site
subprocess.call(["sed -i 's/<\/configuration>//' /usr/local/hadoop/etc/hadoop/yarn-site.xml"],shell=True)

subprocess.call([ "echo  ' <property>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml"], shell=True)

subprocess.call([ "echo  '  <name>yarn.nodemanager.aux-services</name>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml"], shell=True)

subprocess.call([" echo  '  <value>mapreduce_shuffle</value>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml"], shell=True)

subprocess.call([ "echo  ' </property>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml"], shell=True)

subprocess.call([ "echo  ' <property>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml"], shell=True)

subprocess.call([ "echo  '  <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml"], shell=True)

subprocess.call([ "echo  '  <value>org.apache.hadoop.mapred.ShuffleHandler</value>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml"],shell=True)

subprocess.call([" echo  ' </property>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml"], shell=True)

subprocess.call([ "echo  ' <property>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml"], shell=True)

subprocess.call([ "echo   '  <name>yarn.resourcemanager.hostname</name>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml"], shell=True)

subprocess.call([ "echo   '  <value>{}</value>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml".format(masterIP)],shell=True)

subprocess.call([" echo  ' </property>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml"], shell=True)

subprocess.call([ "echo  '</configuration>' >> /usr/local/hadoop/etc/hadoop/yarn-site.xml"], shell=True)


subprocess.call(["sudo mkdir -p $HADOOP_HOME/hadoop_data/hdfs/namenode"],shell=True)
subprocess.call(["sudo touch /usr/local/hadoop/etc/hadoop/masters"],shell=True)
subprocess.call(["sudo echo {} >> /usr/local/hadoop/etc/hadoop/masters".format(masterNode)], shell=True)
subprocess.call(["sudo chown -R ubuntu:ubuntu /usr/local/hadoop"], shell=True)
subprocess.call(["sudo chmod -R 777 /usr/local/hadoop"], shell=True)
##############
subprocess.call([ "sed -i 's/localhost//' /usr/local/hadoop/etc/hadoop/slaves"],shell=True)
##############
for node in workerNodes:
    print node
    subprocess.call(["echo {} >> /usr/local/hadoop/etc/hadoop/slaves".format(node)], shell=True)
