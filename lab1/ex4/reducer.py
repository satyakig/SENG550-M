#!/usr/bin/env python
# reducer.py
# Question 4

import sys

prev_key = None
tot_count = 0

for line in sys.stdin:
    first, word = line.strip().split('.')

    if prev_key is None:
        prev_key = word
        tot_count = 1
        continue

    if prev_key == word:
        tot_count = tot_count + 1
        continue

    if prev_key != word:
        print('%s\t\t%s' % (prev_key, tot_count))
        prev_key = word
        tot_count = 1

print('%s\t\t%s' % (prev_key, tot_count))
