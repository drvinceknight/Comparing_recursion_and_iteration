#!/usr/bin/env python

import matplotlib.pylab as plt
from scipy import stats
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
gradient, intercept, r_value, p_value, std_err = stats.linregress(x, y)
line = [gradient * e + intercept for e in x]
plt.scatter(x, y, label="Basic binary search")
plt.plot(x, line, label="Fitted line: y=%.02fx+%.02f" % (gradient, intercept))
plt.ylim(0, max(y))
x = [e[0] for e in recursivedata]
y = [e[1] for e in recursivedata]
gradient, intercept, r_value, p_value, std_err = stats.linregress(x, y)
line = [gradient * e + intercept for e in x]
plt.scatter(x, y, label="Recursive binary search", color="red")
plt.plot(x, line, label="Fitted line: y=%.02fx+%.02f" % (gradient, intercept), color="red")
plt.ylim(0, max(plt.ylim()[1], max(y)))
plt.legend(loc=2)
plt.savefig("Comparing_binary_search.pdf")
plt.savefig("Comparing_binary_search.png")
