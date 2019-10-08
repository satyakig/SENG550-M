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
# The intermediate key is a combination of the first letter of a word and the word itself
# The intermediate keys are partitioned and sent to the reducers based on the first letter of the word
# All the keys will be sorted automatically by Hadoop since the first letter of the word and the word itself is the key
# Each reducer will get all the words that starts with a specific letter
# The final output will have to be computed separately, using hadoop -getmerge will not give us the final answer

import sys
import re

alphabets = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
}

for line in sys.stdin:
    line = line.strip().lower()
    words = line.split()

    words = list(map(lambda word: re.sub('[^a-zA-Z0-9]', '', word), words))
    words = list(filter(lambda word: len(word) > 0, words))

    for word in words:
        first = word[0]
        if first.isdigit():
            first = 0
        else:
            first = alphabets[first]
        print('%s\t%s' % (first, word))
