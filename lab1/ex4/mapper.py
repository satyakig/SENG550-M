#!/usr/bin/env python
# mapper.py
# Question 4
# Mapper-Reducer solution
# Multi reducer solution
# It can be run using these hadoop options:
#       -D stream.map.output.field.separator=.
#       -D stream.num.map.output.key.fields=2
#       -D mapreduce.map.output.key.field.separator=.
#       -D mapreduce.partition.keypartitioner.options=-k1,1
#       -D mapreduce.job.reduces=27
#       -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
# The intermediate key is a combination based on the first letter of a word and the word itself
# All the keys will be sorted automatically by Hadoop since the first letter of the word and the word itself is the key
# Each reducer will get a set of words that starts with a specific letter or number
# The final output will have to be computed separately, using hadoop -getmerge will not give us the final answer

import sys
import re


for line in sys.stdin:
    line = line.strip().lower()
    words = line.split()

    words = list(map(lambda word: re.sub('[^a-zA-Z0-9]', '', word), words))
    words = list(filter(lambda word: len(word) > 0, words))

    for word in words:
        first_val = word[0]
        if first_val.isdigit():
            first_val = 42

        print('%s.%s' % (first_val, word))
