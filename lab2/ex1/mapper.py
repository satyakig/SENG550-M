#!/usr/bin/env python
# mapper.py
# Question 1
# Map-Reduce solution
import sys

for line in sys.stdin:
    row, col, value = line.strip().lower().split(',')
    print('{}\t{}\t{}'.format(row, col, value))
