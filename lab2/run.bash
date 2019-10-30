#!/usr/bin/env bash
EX=$1

# HDFS Directory
LAB_DIR=satyaki-ghosh-lab2

# Hadoop Stream Command
HADOOP_RUN="$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.6.jar"

echo -e "ASSIGNMENT 2"
echo -e "Setting up HDFS directory: ${LAB_DIR}"
hdfs dfs -mkdir hdfs://$HOSTNAME:9000/${LAB_DIR}/

hdfs dfs -mkdir hdfs://$HOSTNAME:9000/${LAB_DIR}/input/
echo -e "\nUsing Hadoop Stream command: ${HADOOP_RUN}"


if [[ EX -eq 1 ]] || [[ $# -eq 0 ]]
then
echo -e "\nStarting Question 1..."
echo "Copying matrix.txt"
hdfs dfs -copyFromLocal input/matrix.txt /${LAB_DIR}/input/
cd ex1/
hdfs dfs -mkdir hdfs://$HOSTNAME:9000/${LAB_DIR}/ex1/
${HADOOP_RUN} \
    -D mapreduce.job.reduces=0 \
    -files ./mapper.py \
    -input /${LAB_DIR}/input/matrix.txt \
    -output /${LAB_DIR}/ex1/output \
    -mapper ./mapper.py
hadoop fs -getmerge /${LAB_DIR}/ex1/output/ results.txt
echo -e "Partial output:"
tail results.txt
cd ..
echo -e "Completed Question 1"
fi


if [[ EX -eq 2 ]] || [[ $# -eq 0 ]]
then
echo -e "\nStarting Question 2..."
echo "Copying graph.txt"
hdfs dfs -copyFromLocal input/graph.txt /${LAB_DIR}/input/
cd ex2/
hdfs dfs -mkdir hdfs://$HOSTNAME:9000/${LAB_DIR}/ex2/
ITERATION=1
echo -e "Iteration #${ITERATION}:"
${HADOOP_RUN} \
    -D mapreduce.job.reduces=2 \
    -files ./mapper.py,./reducer.py \
    -input /${LAB_DIR}/input/graph.txt \
    -output /${LAB_DIR}/ex2/output${ITERATION} \
    -mapper ./mapper.py \
    -reducer ./reducer.py >> log.txt 2>&1
GRAY_COUNT=$(grep -o 'gray_count' log.txt | wc -l)
echo -e "Gray node count from Iteration #${ITERATION} = ${GRAY_COUNT}"

while [[ GRAY_COUNT -gt 0 ]]
do
echo -e "Iteration #$((ITERATION + 1)):"
rm log.txt
ITERATION=$((ITERATION + 1))
${HADOOP_RUN} \
  -D mapreduce.job.reduces=2 \
  -files ./mapper.py,./reducer.py \
  -input /${LAB_DIR}/ex2/output$((ITERATION - 1))/ \
  -output /${LAB_DIR}/ex2/output${ITERATION} \
  -mapper ./mapper.py \
  -reducer ./reducer.py >> log.txt 2>&1
GRAY_COUNT=$(grep -o 'gray_count' log.txt | wc -l)
echo -e "Gray node count from Iteration #${ITERATION} = ${GRAY_COUNT}"
done
hadoop fs -getmerge /${LAB_DIR}/ex2/output${ITERATION}/ results.txt
echo -e "White node count from Iteration #${ITERATION} = $(grep -o 'white_count' log.txt | wc -l)"
echo -e "Black node count from Iteration #${ITERATION} = $(grep -o 'black_count' log.txt | wc -l)"
rm log.txt
echo -e "Output:"
cat results.txt
cd ..
echo -e "Completed Question 2"
fi


if [[ EX -eq 3 ]] || [[ $# -eq 0 ]]
then
echo -e "\nStarting Question 3..."
echo "Copying retail.dat"
hdfs dfs -copyFromLocal input/retail.dat /${LAB_DIR}/input/
cd ex3/
hdfs dfs -mkdir hdfs://$HOSTNAME:9000/${LAB_DIR}/ex3/
${HADOOP_RUN} \
    -D mapreduce.job.reduces=10 \
    -D stream.num.map.output.key.fields=2 \
    -D mapreduce.partition.keypartitioner.options=-k1,1 \
    -files ./mapper.py,./reducer.py \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
    -input /${LAB_DIR}/input/retail.dat \
    -output /${LAB_DIR}/ex3/output \
    -mapper ./mapper.py \
    -reducer ./reducer.py
hadoop fs -getmerge /${LAB_DIR}/ex3/output/ results.txt
echo -e "Partial output:"
tail results.txt
cd ..
echo -e "Completed Question 3"
fi

echo -e "\nCleaning up"
hdfs dfs -rm -r hdfs://$HOSTNAME:9000/${LAB_DIR}/
echo -e "Completed"
