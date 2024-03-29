# bch-sigchecks-stats

Statistics on SigChecks, a replacement for SigOps

These are various python files for analyzing a large dataset derived from the BCH blockchain (which was ~200 GB at time of scan).

- First, [download the dataset (~500 MB file)](https://mega.nz/#!DJNwAAyB!K9kw_8uDBR4hZZEor53V4OKiQZgsppge-LFvVPkWVI8).
- Then, run the various analysis*.py scripts which boil down the data into even smaller files for plotting.
- Then, run the corresponding plot*.py script.

## Dataset

This has the following format. Each line is a transaction, except for the lines starting in # which indicate a change of block:
```
...
# 1234                <- the following transactions come from block 1234
- 456 100 2 50 1      <- a transaction of size 456 had two inputs: one with scriptsig length 100 and 2 sigchecks, the other with scriptsig length 50 and 1 sigchecks
- 876 100 1 100 1 100 1 100 1  <- another transaction
892bb6f09ed2ad140c48703aa71f1830273afb50c3c68f0d92d26045df47d15a 930 148 9 654 9    <- a notable transaction due to many sigchecks! instead of -, the txid is given
...
# 1235                <- end of block 1234; the following transactions come from block 1235
...
```

## Collection

The data was collected using the patch found in this directory. It works by completely disabling script cache lookups during ConnectBlock. To use this patch, set up a new node (for compactness and efficiency, set it up in pruning and blocksonly mode) that feeds only from your main node, and run it with assumevalid off. This will take some time as it needs to fully validate the blockchain.

Please note that the patch is old and predates the schnorr multisig upgrade.
