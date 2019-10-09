#!/usr/bin/env python
# mapper.py
# Question 3
# Map-Reduce solution
# The intermediate key is the word and the file name, the value is empty

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
        print('%s %s\t%s' % (word, file_name, 1))
