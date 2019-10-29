#!/usr/bin/env python
# mapper.py
# Question 1
# Map only solution
# -D mapreduce.job.reduces=0
import sys

for line in sys.stdin:
    row, col, value = line.strip().lower().split(',')
    print('{}\t{}\t{}'.format(col, row, value))
