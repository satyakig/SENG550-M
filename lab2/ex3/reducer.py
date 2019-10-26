#!/usr/bin/env python
# reducer.py
# Question 3
import sys

prev_i = ''
prev_j = ''
pair_count = 0
i_count = 0


def log():
    if prev_i != '' and prev_j != '' and pair_count != 0 and i_count != 0:
        print('f({}|{}) = {}'.format(prev_j, prev_i, float(pair_count) / float(i_count)))


for line in sys.stdin:
    line = line.strip()

    if 'pair' not in line:
        i, count = line.split()

        if prev_i != i:
            log()
            prev_i = i
            prev_j = ''
            pair_count = 0
            i_count = int(count)
        else:
            i_count = i_count + int(count)
    else:
        i, j = line.strip().split()[:2]
        if j != prev_j:
            log()
            prev_j = j
            pair_count = 1
        else:
            pair_count = pair_count + 1

log()
