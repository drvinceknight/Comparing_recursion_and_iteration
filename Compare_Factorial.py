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
    i = 1
    while i <= n:
        r *= i
        i += 1
    return r


def recursivefactorial(n):
    if n == 1:
        return 1
    return n * recursivefactorial(n - 1)


if __name__ == "__main__":
    import sys
    import csv
    N = 10000000
    sys.setrecursionlimit(N)
    f = open("factorial.csv", "a")
    datafile = csv.writer(f)
    for n in xrange(1, N + 1):
        print "Calculating %s!" % n
        t = timeit('factorial(n)')
        print "\t base: %.04f seconds" % t
        r = timeit('recursivefactorial(n)')
        print "\t recursive: %.04f seconds" % r
        datafile.writerow([n, t, r])
    f.close()
