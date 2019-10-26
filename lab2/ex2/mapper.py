#!/usr/bin/env python
# mapper.py
# Question 2
# Map-Reduce solution
# Multi iteration solution
import sys

WHITE = 'white'
GRAY = 'gray'
BLACK = 'black'

for line in sys.stdin:
    nid, values = line.strip().lower().split()
    adj, score, colour, parent = values.split('|')

    try:
        score = int(score)
    except ValueError:
        score = sys.maxsize

    if colour == GRAY:
        colour = BLACK

        if adj != 'null':
            adj_list = list(
                map(lambda child: int(child.strip()), adj.split(',')))
            for node in adj_list:
                print('{}\t{}|{}|{}|{}'.format(
                    node, 'null', score + 1, GRAY, nid))

    print('{}\t{}|{}|{}|{}'.format(nid, adj, score, colour, parent))
