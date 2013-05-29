#!/usr/bin/env python
"""
Script to compare factorial  in recursion and non recursion
"""
from __future__ import division
import time


def mean(list):
    return sum(list) / len(list)


def timeit(code, trials=10):
    t = []
    for i in range(trials):
        start_time = time.time()
        eval(code)
        t.append(time.time() - start_time)
    return mean(t)


def factorial(n):
    r = 1
    for i in xrange(2, n + 1):
        r *= i
    return r


def recursivefactorial(n):
    if n == 1:
        return 1
    return n * recursivefactorial(n - 1)


if __name__ == "__main__":
    import sys
    import csv
    N = 1000000
    timings = []
    sys.setrecursionlimit(100000)
    for n in xrange(1, N + 1):
        print "Calculating %s!" % n
        t = timeit('factorial(n)')
        print "\t base: %.04f seconds" % t
        r = timeit('recursivefactorial(n)')
        print "\t recursive: %.04f seconds" % r
        timings.append([n, t, r])
    f = open("factorial.csv", "rb")
    datafile = csv.writer(f)
    for row in timings:
        datafile.writerow(f)
    f.close()
