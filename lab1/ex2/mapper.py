#!/usr/bin/env python
# mapper.py
# Question 2
# Map-Reduce solution
# It can be run using the standard hadoop mapper reducer configuration
# The intermediate key is a combination of the two consecutive words

import sys
import re

for line in sys.stdin:
    line = line.strip().lower()
    words = line.split()

    words = list(map(lambda word: re.sub('[^a-zA-Z0-9]', '', word), words))
    words = list(filter(lambda word: len(word) > 0, words))
    words_len = len(words)

    if words_len > 1:
        for index, word in enumerate(words):
            if index < words_len - 1:
                print('%s %s\t%s' % (word, words[index + 1], 1))
