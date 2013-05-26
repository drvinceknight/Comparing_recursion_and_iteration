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


def binarysearch(data, target):
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


def recursivebinarysearch(data, target, first, last):
    """
    Code that carries out a recursive binary search
    """
    if first > last:
        return False
    index = int((first + last) / 2)
    if target == data[index]:
        return index
    if target < data[index]:
        return recursivebinarysearch(data, target, first, index - 1)
    else:
        return recursivebinarysearch(data, target, index + 1, last)
    return index


class Datastore():
    """
    Class to hold the data.
    """
    def __init__(self, data):
        self.rawdata = data
        self.basedata = []
        self.recursivedata = []
        for row in data:
            k = 0
            for e in row[1:]:
                if k % 2 == 0:
                    self.basedata.append([row[0], e])
                else:
                    self.recursivedata.append([row[0], e])
                k += 1


if __name__ == '__main__':
    maxdatasize = 50
    timings = []
    recursivetimings = []
    for k in range(1, maxdatasize + 1):
        print "Searching arrays of size %s" % k
        timings.append([k])
        data = range(k)
        for target in range(k):
            timings[-1].append(timeit('binarysearch(data, target)'))
            timings[-1].append(timeit('recursivebinarysearch(data, target, 0, len(data) - 1)'))

    # Pickle data

    print "Creating datastore"
    datastore = Datastore(timings)
    print "Writing files to csv"
    f = open("binarysearch.csv", "w")
    outfile = writer(f)
    for row in datastore.basedata:
        outfile.writerow(row)
    f.close()
    f = open("recursivebinarysearch.csv", "w")
    outfile = writer(f)
    for row in datastore.recursivedata:
        outfile.writerow(row)
    f.close()
