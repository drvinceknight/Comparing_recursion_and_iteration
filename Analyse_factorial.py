#!/usr/bin/env python

"""
Script to analyse the factorial.csv file
"""

from __future__ import division
import matplotlib.pyplot as plt
import csv
from scipy import interpolate

print "Importing data from 'factorial.csv'"
with open("factorial.csv", "rb") as f:
    data = csv.reader(f)
    data = [row for row in data]
    data = [[eval(row[0]), eval(row[1]), eval(row[2])] for row in data]

print "Plotting scatter plots"
x = []
y1 = []
y2 = []
yc = []
for row in data:
    x.append(row[0])
    y1.append(row[1])
    y2.append(row[2])
    yc.append(row[1] / row[2])

print "Interpolating"
tck = interpolate.splrep(x, y1, s=1)
y1new = interpolate.splev(x, tck, der=0)
tck = interpolate.splrep(x, y2, s=1)
y2new = interpolate.splev(x, tck, der=0)

print "Plotting"
fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.scatter(x, y1, s=.2)
ax1.plot(x, y1new, label="Iterative", linewidth=2)
ax1.scatter(x, y2, color="red", s=.2)
ax1.plot(x, y2new, color="red", label="Recursive", linewidth=2)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax1.set_xlabel("$n$")
ax1.set_ylabel("Time (seconds)")

ax2 = ax1.twinx()
ax2.plot(x, yc, color="Black", label="Ratio")
ax2.set_ylabel("Ratio of iterative to recursive time")

plt.plot(x, [1 for e in x], color="Green", linestyle="dashed")
plt.ylim(0, plt.ylim()[1])
plt.xlim(0, plt.xlim()[1])
plt.legend(loc=2)
plt.savefig("factorial.png", bbox_inches='tight')
plt.savefig("factorial.pdf", bbox_inches='tight')
