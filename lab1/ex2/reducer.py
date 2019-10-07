#!/usr/bin/env python
# reducer.py
# Question 2

import sys

prev_key = (None, None)
tot_count = 0

for line in sys.stdin:
    word1, word2, count = line.strip().split()

    if prev_key == (None, None):
        prev_key = (word1, word2)
        tot_count = int(count)
        continue

    if prev_key == (word1, word2):
        tot_count = tot_count + int(count)
        continue

    if prev_key != (word1, word2):
        print('%s %s\t\tCount: %s' % (prev_key[0], prev_key[1], tot_count))
        prev_key = (word1, word2)
        tot_count = int(count)

print('%s %s\t\tCount: %s' % (prev_key[0], prev_key[1], tot_count))
