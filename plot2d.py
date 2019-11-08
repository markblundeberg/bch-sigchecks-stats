#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

dcount = np.loadtxt('c2d.txt', dtype=int)
print(dcount.shape)

print('max', np.amax(dcount))
print('total', np.sum(dcount))
uncounted = 0

# Squashed down on sigchecks axis
#dsquashsc = np.sum(dcount, axis=0)
#print((dsquashsc != 0)*1)
#print(dsquashsc)

# Which input had 20 sigchecks?
#print(np.argmax(dcount[:,20]))

# trim off right rows
cmisc = dcount[:, 21:]
dcount = dcount[:, :21]

print("uncounted over 20 sigchecks:", np.sum(cmisc))
uncounted += np.sum(cmisc)

# trim off top rows
cmisc = dcount[1000:, :]
dcount = dcount[:1000, :]

print("uncounted remainder (1000 bytes or longer):", np.sum(cmisc))

uncounted += np.sum(cmisc)

fig = plt.figure()
fig.set_size_inches(8,12)

plt.imshow(dcount*1.0, origin='lower', norm=LogNorm(0.9, 200e6), aspect='auto')

plt.autoscale(False)

cb = plt.colorbar()
cb.set_label("number of inputs")

plt.xlabel("number of sigchecks")
plt.ylabel("length of scriptsig")

plx = np.arange(21.)
proplimit = np.maximum(plx*43 - 60 , plx*23)
if True:
    # plt.plot(plx, plx*40, color='k', marker='o', lw=0.5, ms=1, label="special recording")
    plt.plot(plx[3:16], 3*72.5 + 6 + plx[3:16]*34, color='r', marker='o', lw=0.5, ms=1, label="p2sh-multisig 3-of-N")
    plt.plot(plx[2:16], 2*72.5 + 6 + plx[2:16]*34, color='r', marker='o', lw=0.5, ms=1, label="p2sh-multisig 2-of-N")
    plt.plot(plx[1:16], 1*72.5 + 6 + plx[1:16]*34, color='r', marker='o', lw=0.5, ms=1, label="p2sh-multisig 1-of-N")
    plt.plot(plx[1:4], 72.5 + 0*plx[1:4], color='m', marker='o', ls='none', ms=3, label="bare-multisig 1-of-N")
    plt.plot(plx, 100*plx, color='g', marker='o', lw=0.5, ms=1, label="p2pkh/p2sh normal-schnorr")
    plt.plot(plx[1:], plx[1:]*66, color='g', marker='s', lw=0.5, ms=1, label="p2pk/p2ms bare-schnorr")
    plt.plot(plx, proplimit, color='b', marker='o', lw=0.5, ms=1, label="proposed limit")

    plt.legend(loc='upper right')

plt.savefig('plot2d.png', dpi=200)


print("uncounted:", uncounted)
