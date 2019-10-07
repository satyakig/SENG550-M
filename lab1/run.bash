#!/usr/bin/env bash

# HDFS Directory
LAB_DIR=satyaki-ghosh-lab1

# Hadoop Stream Command
HADOOP_RUN="$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.6.jar"

echo -e "Setting up HDFS directory: ${LAB_DIR}"
hdfs dfs -mkdir hdfs://$HOSTNAME:9000/${LAB_DIR}/

echo -e "\nCopying files to HDFS..."
cd text/
hdfs dfs -mkdir hdfs://$HOSTNAME:9000/${LAB_DIR}/text/
echo "shakespeare.txt"
hdfs dfs -copyFromLocal ./shakespeare.txt /${LAB_DIR}/text/
echo "iliad.txt"
hdfs dfs -copyFromLocal ./iliad.txt /${LAB_DIR}/text/
echo "jane.txt"
hdfs dfs -copyFromLocal ./jane.txt /${LAB_DIR}/text/
echo "moby.txt"
hdfs dfs -copyFromLocal ./moby.txt /${LAB_DIR}/text/
cd ..


echo -e "\nUsing Hadoop Stream command: ${HADOOP_RUN}"
echo -e "\nStarting Question 1..."
cd ex1/
hdfs dfs -mkdir hdfs://$HOSTNAME:9000/${LAB_DIR}/ex1/
${HADOOP_RUN} \
  -D mapreduce.job.reduces=0 \
  -files ./mapper.py \
  -input /${LAB_DIR}/text/shakespeare.txt \
  -output /${LAB_DIR}/ex1/output \
  -mapper ./mapper.py
hadoop fs -getmerge /${LAB_DIR}/ex1/output/ results.txt
echo -e "Partial output:"
tail results.txt
cd ..
echo -e "Completed Question 1"


echo -e "\nStarting on Question 2..."
cd ex2/
hdfs dfs -mkdir hdfs://$HOSTNAME:9000/${LAB_DIR}/ex2/
${HADOOP_RUN} \
  -files ./mapper.py,./reducer.py \
  -input /${LAB_DIR}/text/shakespeare.txt \
  -output /${LAB_DIR}/ex2/output \
  -mapper ./mapper.py \
  -reducer ./reducer.py
hadoop fs -getmerge /${LAB_DIR}/ex2/output/ results.txt
echo -e "Partial output:"
tail results.txt
cd ..
echo -e "Completed Question 2"


echo -e "\nStarting on Question 3..."
cd ex3/
hdfs dfs -mkdir hdfs://$HOSTNAME:9000/${LAB_DIR}/ex3/
${HADOOP_RUN} \
  -files ./mapper.py,./reducer.py \
  -input /${LAB_DIR}/text/ \
  -output /${LAB_DIR}/ex3/output \
  -mapper ./mapper.py \
  -combiner ./reducer.py \
  -reducer ./reducer.py
hadoop fs -getmerge /${LAB_DIR}/ex3/output/ results.txt
echo -e "Partial output:"
tail results.txt
cd ..
echo -e "Completed Question 3"


echo -e "\nStarting on Question 4..."
cd ex4/
hdfs dfs -mkdir hdfs://$HOSTNAME:9000/${LAB_DIR}/ex4/
${HADOOP_RUN} \
  -D stream.map.output.field.separator=. \
  -D stream.num.map.output.key.fields=2 \
  -D mapreduce.map.output.key.field.separator=. \
  -D mapreduce.partition.keypartitioner.options=-k1,1 \
  -D mapreduce.job.reduces=27 \
  -files ./mapper.py,./reducer.py \
  -input /${LAB_DIR}/text/ \
  -output /${LAB_DIR}/ex4/output \
  -mapper ./mapper.py \
  -reducer ./reducer.py \
  -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
hdfs dfs -copyToLocal /${LAB_DIR}/ex4/output ./
hadoop fs -getmerge /${LAB_DIR}/ex4/output/ results.txt
echo -e "Partial output:"
tail results.txt
cd ..
echo -e "Completed Question 4"

echo -e "\nCleaning up"
hdfs dfs -rm -r hdfs://$HOSTNAME:9000/${LAB_DIR}/
echo -e "Completed"
