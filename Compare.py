#!/usr/bin/env python
"""
Script to compare binary search written with recursive and non recursive code
"""

from __future__ import divison
import time
import random
import pickle


def mean(list):
    return sum(list) / len(list)


def timeit(code, trials=10):
    t = []
    for i in range(trials):
        start_time = time.time()
        eval(code)
        t.append(time.time() - start_time)
    return mean(t)


def binarysearch(data, target):
    """
    Code that carries out a random binary search
    """
    return index


def recursivebinarysearch(data, target):
    return index

if __name__ == '__main__':
    maxdatasize = 1000
    numberofsorts = 100
    timings = []
    recursivetimings = []
    for k in range(maxdatasize):
        timings.append([k + 1])
        recursivetimings.append([k + 1])
        for i in numberofsorts:
            data = range(k)
            target = random.choice(data)
            timings[-1].append(timeit('binarysearch(data, target)'))
            recursivetimings[-1].append(timeit('recursivebinarysearch(data, target)'))
    # Pickle data
