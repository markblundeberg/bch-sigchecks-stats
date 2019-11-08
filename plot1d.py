#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

dcount = np.loadtxt('densitytx.txt', dtype=int)

# strip off the last one
overlimit = dcount[-1]
dcount = dcount[:-1]

print(f"{overlimit} were over {len(dcount)}")
print(dcount.shape)

edges = np.arange(len(dcount)+1)

print('max', np.amax(dcount), '@', np.argmax(dcount))
print('total', np.sum(dcount))

plt.bar(edges[:-1], dcount, align='edge', width=np.diff(edges))

plt.yscale("log")
plt.ylim(0.5, None)
plt.xlim(0, len(dcount))

plt.xlabel("1/density (bytes per SigCheck)")
plt.ylabel("how many transactions")

plt.savefig('plot1d.png', dpi=200)

