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

