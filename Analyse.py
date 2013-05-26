#!/usr/bin/env python

from Compare import Datastore
import matplotlib.pylab as plt
import pickle

print "Unpickling datastore.pickle"
f = open("datastore.pickle", "r")
datastore = pickle.load(f)
f.close()

x = [e[0] for e in datastore.basedata]
y = [e[1] for e in datastore.basedata]
plt.figure()
x = [e[0] for e in datastore.basedata]
y = [e[1] for e in datastore.basedata]
plt.scatter(x, y, label="Basic binary search")
plt.ylim(0, max(y))
x = [e[0] for e in datastore.recursivedata]
y = [e[1] for e in datastore.recursivedata]
plt.scatter(x, y, label="Recursive binary search", color="red")
plt.ylim(0, max(plt.ylim()[1], max(y)))
plt.legend(loc=2)
plt.savefig("Comparing_binary_search.pdf")
