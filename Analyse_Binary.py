#!/usr/bin/env python

from __future__ import division
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

print "Drawing plot with all points"
plt.figure()
x = [e[0] for e in basedata]
y = [e[1] for e in basedata]
gradient, intercept, r_value, p_value, std_err = stats.linregress(x, y)
line = [gradient * e + intercept for e in x]
plt.scatter(x, y, label="Iterative")
plt.plot(x, line, label="Fitted line: y=%.05fx+%.05f" % (gradient, intercept))
plt.ylim(0, max(y))
x = [e[0] for e in recursivedata]
y = [e[1] for e in recursivedata]
gradient, intercept, r_value, p_value, std_err = stats.linregress(x, y)
line = [gradient * e + intercept for e in x]
plt.scatter(x, y, label="Recursive", color="red")
plt.plot(x, line, label="Fitted line: y=%.05fx+%.05f" % (gradient, intercept), color="red")
plt.ylim(0, max(plt.ylim()[1], max(y)))
plt.xlabel("Size of dataset")
plt.ylabel("Time (seconds)")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.savefig("binary_all_data.pdf", bbox_inches='tight')
plt.savefig("binary_all_data.png", bbox_inches='tight')

print "Drawing plot of means"


def mean(data):
    return sum(data) / len(data)

n = {}
means = {}
for e in basedata:
    if e[0] in n:
        n[e[0]] += 1
        means[e[0]] += e[1]
    else:
        n[e[0]] = 1
        means[e[0]] = e[1]

recursive_means = {}
for e in recursivedata:
    if e[0] in recursive_means:
        recursive_means[e[0]] += e[1]
    else:
        recursive_means[e[0]] = e[1]

for key in n:
    means[key] /= n[key]
    recursive_means[key] /= n[key]

plt.figure()
x = [key for key in n]
y1 = [means[key] for key in n]
y2 = [recursive_means[key] for key in n]
gradient, intercept, r_value, p_value, std_err = stats.linregress(x, y1)
line = [gradient * e + intercept for e in x]
plt.scatter(x, y1, label="Basic binary search")
plt.plot(x, line, label="Fitted line: y=%.05fx+%.05f" % (gradient, intercept))
plt.ylim(0, max(y1))
gradient, intercept, r_value, p_value, std_err = stats.linregress(x, y2)
line = [gradient * e + intercept for e in x]
plt.scatter(x, y2, label="Recursive binary search", color="red")
plt.plot(x, line, label="Fitted line: y=%.05fx+%.05f" % (gradient, intercept), color="red")
plt.ylim(0, max(plt.ylim()[1], max(y2)))
plt.xlabel("Size of dataset")
plt.ylabel("Time (seconds)")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.savefig("binary_mean.pdf", bbox_inches='tight')
plt.savefig("binary_mean.png", bbox_inches='tight')
