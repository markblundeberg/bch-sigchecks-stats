#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import gzip

dcount = np.zeros((301,), dtype=np.uint64)
maxd = len(dcount)-1

stopheight = 1000000
with gzip.open('realsigopinputs-585795.txt.gz', 'rt') as f:
    for line in f:
        if not line:
            continue
        if line[0] == '#':
            bh = int(line[1:])
            if bh % 100000 == 0:
                print('height =',bh)
                np.savetxt('densitytx-%d.txt'%(bh), dcount, fmt='%d')
            if bh > stopheight:
                break
            continue
        inpdatastrings = line.split()

        txsize = int(inpdatastrings[1])
        sigchecks = sum(int(s) for s in inpdatastrings[3::2])
        try:
            density = min(maxd, int(txsize)//int(sigchecks))
        except ZeroDivisionError:
            density = maxd
        dcount[density] += 1

np.savetxt('densitytx.txt', dcount, fmt='%d')

print(np.sum(dcount))

