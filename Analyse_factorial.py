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
for row in data:
    x.append(row[0])
    y1.append(row[1])
    y2.append(row[2])

print "Interpolating"
tck = interpolate.splrep(x, y1, s=1)
y1new = interpolate.splev(x, tck, der=0)
tck = interpolate.splrep(x, y2, s=1)
y2new = interpolate.splev(x, tck, der=0)

plt.scatter(x, y1, s=.2)
plt.plot(x, y1new, label="Base", linewidth=2)
plt.scatter(x, y2, color="red", s=.2)
plt.plot(x, y2new, color="red", label="Recursive", linewidth=2)
plt.legend(loc=2)
plt.xlabel("$n!$")
plt.savefig("factorial.png")
