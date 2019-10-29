#!/usr/bin/env python
# mapper.py
# Question 3
# Map-Reduce solution
# -D mapreduce.job.reduces=10
# -D stream.num.map.output.key.fields=2
# -D mapreduce.partition.keypartitioner.options=-k1, 1
# -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
import sys
import itertools
import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return int(numer / denom)


for line in sys.stdin:
    nums = list(map(lambda num: num, line.strip().lower().split()))
    combinations = list(itertools.combinations(nums, 2))
    num_length = len(nums)
    i_count = 0

    if num_length > 1:
        i_count = ncr(num_length - 1, num_length - 2)

    for j, i in combinations:
        print('{}\t{}\tpair'.format(j, i))
        print('{}\t{}\tpair'.format(i, j))

    for i in nums:
        print('{}\t\t{}'.format(i, i_count))
