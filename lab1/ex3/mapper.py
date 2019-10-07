#!/usr/bin/env python
# mapper.py
# Question 3
# Map-Reduce solution
# It can be run using the standard hadoop mapper reducer configuration (reducer can also be used a combiner)
# The intermediate key is the word

import os
import sys
import re

for line in sys.stdin:
    line = line.strip().lower()
    words = line.split()

    words = list(map(lambda word: re.sub('[^a-zA-Z0-9]', '', word), words))
    words = list(filter(lambda word: len(word) > 0, words))
    full_path = os.environ['mapreduce_map_input_file']
    splits = full_path.split('/')
    file_name = splits[len(splits) - 1]

    for word in words:
        print('%s\t%s' % (word, file_name))
