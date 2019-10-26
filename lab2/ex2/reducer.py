#!/usr/bin/env python
# reducer.py
# Question 2
import sys

WHITE = 'white'
GRAY = 'gray'
BLACK = 'black'

colour_map = {
    WHITE: 0,
    GRAY: 1,
    BLACK: 2,
}

prev_nid = None
prev_adj = 'null'
prev_score = sys.maxsize
prev_colour = WHITE
prev_parent = 'null'

for line in sys.stdin:
    nid, values = line.strip().split()
    adj, score, colour, parent = values.split('|')
    score = int(score)

    if prev_nid is None:
        prev_nid = nid
        prev_adj = adj
        prev_score = score
        prev_colour = colour
        prev_parent = parent

    if prev_nid == nid:
        if adj != 'null':
            prev_adj = adj
        if colour_map[colour] > colour_map[prev_colour]:
            prev_colour = colour
        if score < prev_score:
            prev_score = score
            prev_parent = parent

    if prev_nid != nid:
        print('{}\t{}|{}|{}|{}'.format(prev_nid, prev_adj,
                                       prev_score, prev_colour, prev_parent))
        if prev_colour == WHITE:
            print >> sys.stderr, 'reporter:counter:BFS,white_count,1'
        if prev_colour == GRAY:
            print >> sys.stderr, 'reporter:counter:BFS,gray_count,1'
        if prev_colour == BLACK:
            print >> sys.stderr, 'reporter:counter:BFS,black_count,1'

        prev_nid = nid
        prev_adj = adj
        prev_score = score
        prev_colour = colour
        prev_parent = parent

if prev_nid is not None:
    print('{}\t{}|{}|{}|{}'.format(prev_nid, prev_adj,
                                   prev_score, prev_colour, prev_parent))
    if prev_colour == WHITE:
        print >> sys.stderr, 'reporter:counter:BFS,white_count,1'
    if prev_colour == GRAY:
        print >> sys.stderr, 'reporter:counter:BFS,gray_count,1'
    if prev_colour == BLACK:
        print >> sys.stderr, 'reporter:counter:BFS,black_count,1'
