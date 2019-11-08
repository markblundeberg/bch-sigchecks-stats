#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import gzip

dcount = np.zeros((2002,202), dtype=np.uint64)
maxsize = dcount.shape[0] - 1
maxsigc = dcount.shape[1] - 1

stopheight = 1000000
fspecial = open('specials-gen.txt', 'w')
txnum=0
icount = 0
lastcount = dcount*0
with gzip.open('realsigopinputs-585795.txt.gz', 'rt') as f:
    for line in f:
        if not line:
            continue
        if line[0] == '#':
            if icount != np.sum(dcount) or np.any(dcount < lastcount):
                np.savetxt('c2d-lastgood.txt', lastdcount, fmt='%d')
                np.savetxt('c2d-bad.txt', dcount, fmt='%d')
                raise RuntimeError('Bad count!', bh)
            txnum=0
            bh = int(line[1:])
            if bh % 10000 == 0:
                print('height =',bh)
                np.savetxt('c2d-%d.txt'%(bh), dcount, fmt='%d')
            if bh > stopheight:
                break
            lastdcount = dcount.copy()
            continue
        txid, txsize, inpdatastr = line.split(maxsplit=2)

        inpdata = np.fromstring(inpdatastr, dtype=int, sep=' ')
        inpdata.shape = (-1,2)
        sizes = inpdata[:,0]
        sigchecks = inpdata[:,1]

        # compare to proposed limit
        minsize = np.maximum(sigchecks*43 - 60 , sigchecks*23)
        if np.any(sizes < minsize):
            fspecial.write("#%d\n"%(bh))
            fspecial.write(line)

        np.clip(sizes, 0, maxsize, out=sizes)
        np.clip(sigchecks, 0, maxsigc, out=sigchecks)

        np.add.at(dcount, [sizes, sigchecks], 1)
        icount += len(sizes)
        txnum += 1
        if bh > 500000 and dcount[145, 16] == 0:
            np.savetxt('c2d-bad.txt', dcount, fmt='%d')
            raise RuntimeError('Lost point!', bh, txnum, line, sizes, sigchecks)

np.savetxt('c2d.txt', dcount, fmt='%d')

print(np.sum(dcount))

