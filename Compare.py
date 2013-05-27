#!/usr/bin/env python
"""
Script to compare binary search written with recursive and non recursive code
"""

from __future__ import division
import time
from csv import writer


def mean(list):
    return sum(list) / len(list)


def timeit(code, trials=10):
    t = []
    for i in range(trials):
        start_time = time.time()
        eval(code)
        t.append(time.time() - start_time)
    return mean(t)


data = range(10)


def binarysearch(target):
    """
    Code that carries out a binary search
    """
    first = 0
    last = len(data) - 1
    found = False
    while first <= last and not found:
        index = int((first + last) / 2)
        if target == data[index]:
            found = True
        elif target < data[index]:
            last = index - 1
        else:
            first = index + 1
    return index


def recursivebinarysearch(target, first, last):
    """
    Code that carries out a recursive binary search
    """
    if first > last:
        return False
    index = int((first + last) / 2)
    if target == data[index]:
        return index
    if target < data[index]:
        return recursivebinarysearch(target, first, index - 1)
    else:
        return recursivebinarysearch(target, index + 1, last)
    return index


if __name__ == '__main__':
    maxdatasize = 5000
    timings = []
    recursivetimings = []
    f = open("binarysearch.csv", "a")
    outfile = writer(f)
    rf = open("recursivebinarysearch.csv", "a")
    rec_outfile = writer(rf)
    for k in range(1, maxdatasize + 1, 10):
        print "Searching arrays of size %s" % k
        timings.append([k])
        data = range(k)
        for target in range(k):
            t = timeit('binarysearch(target)')
            rt = timeit('recursivebinarysearch(target, 0, len(data) - 1)')
            outfile.writerow([k, t])
            rec_outfile.writerow([k, rt])
    f.close()
    rf.close()
