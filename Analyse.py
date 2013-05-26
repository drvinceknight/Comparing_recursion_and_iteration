#!/usr/bin/env python

import matplotlib.pylab as plt
from csv import reader

print "Reading data"
f = open("binarysearch.csv", "r")
basedata = reader(f)
basedata = [[eval(row[0]), eval(row[1])] for row in basedata]
f.close()

f = open("recursivebinarysearch.csv", "r")
recursivedata = reader(f)
recursivedata = [[eval(row[0]), eval(row[1])] for row in recursivedata]
f.close()

print "Drawing plot"
plt.figure()
x = [e[0] for e in basedata]
y = [e[1] for e in basedata]
plt.scatter(x, y, label="Basic binary search")
plt.ylim(0, max(y))
x = [e[0] for e in recursivedata]
y = [e[1] for e in recursivedata]
plt.scatter(x, y, label="Recursive binary search", color="red")
plt.ylim(0, max(plt.ylim()[1], max(y)))
plt.legend(loc=2)
plt.savefig("Comparing_binary_search.pdf")
