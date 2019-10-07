#!/usr/bin/env python
# reducer.py
# Question 3

import sys

prev_key = None
file_names = ''

for line in sys.stdin:
    word, files = line.strip().split()

    if prev_key is None:
        prev_key = word
        file_names = files
        continue

    if prev_key == word:
        multi_files = files.split(',')
        for file in multi_files:
            if file not in file_names:
                file_names = file_names + ', ' + file
        continue

    if prev_key != word:
        arr = file_names.split(', ')
        arr.sort()
        print('%s\t%s' % (prev_key, ', '.join(arr)))
        prev_key = word
        file_names = files

arr = file_names.split(', ')
arr.sort()
print('%s\t%s' % (prev_key, ', '.join(arr)))
