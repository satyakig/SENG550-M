#!/usr/bin/env python
# mapper.py
# Question 1
# Map only solution
# It can be run using these hadoop options:
#       -D mapreduce.job.reduces=0

import string
import sys
import random

for line in sys.stdin:
    line = line.strip()

    if (random.random() < 0.1):
        print('%s\t%s' % (line, ''))
