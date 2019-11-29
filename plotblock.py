#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

dat = np.loadtxt('blockstats.txt.gz')

bins = np.arange(301)

print("total density: ", np.sum(dat[:,0])/np.sum(dat[:,1]))

plt.hist(dat[:,0]/dat[:,1],  bins = np.arange(301))

plt.yscale("log")

plt.xlabel("1/density (bytes per SigCheck)")
plt.ylabel("how many blocks")

plt.savefig('plotblk.png', dpi=200)

plt.figure()

maxidx = np.argmax(dat[:, 1])
print("max sigchecks: ", dat[maxidx, 1], "in block", maxidx)
plt.hist(dat[:, 1], bins = np.arange(0, 250001, 1000))

plt.yscale("log")

plt.xlabel("how many sigchecks in the block")
plt.ylabel("how many blocks")

plt.savefig('plotblktot.png', dpi=200)
