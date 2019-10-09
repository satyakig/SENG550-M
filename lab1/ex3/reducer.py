#!/usr/bin/env python
# reducer.py
# Question 3

import sys

prev_key = None
file_names = ''

for line in sys.stdin:
    word, file, count = line.strip().split()

    if prev_key is None:
        prev_key = word
        file_names = file
        continue

    if prev_key == word:
        if file not in file_names:
            file_names = file_names + ', ' + file
        continue

    if prev_key != word:
        print('%s\t%s' % (prev_key, file_names))
        prev_key = word
        file_names = file

print('%s\t%s' % (prev_key, file_names))
