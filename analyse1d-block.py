#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import gzip

sumsize = 0
sumsigchecks = 0
fout = open("blockstats.txt", 'w')
with gzip.open('realsigopinputs-585795.txt.gz', 'rt') as f:
    for line in f:
        if not line:
            continue
        if line[0] == '#':
            bh = int(line[1:])
            if bh % 100000 == 0:
                print('height =',bh)
            fout.write(f'{sumsize} {sumsigchecks}\n')
            sumsize = 0
            sumsigchecks = 0
            continue
        inpdatastrings = line.split()
        txsize = int(inpdatastrings[1])
        sigchecks = sum(int(s) for s in inpdatastrings[3::2])
        sumsize += txsize
        sumsigchecks += sigchecks

fout.write(f'{sumsize} {sumsigchecks}\n')
