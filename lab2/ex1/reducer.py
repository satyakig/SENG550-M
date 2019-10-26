#!/usr/bin/env python
# reducer.py
# Question 1
import sys

for line in sys.stdin:
    row, col, value = line.strip().split()
    print('{}\t{}\t{}'.format(col, row, value))
