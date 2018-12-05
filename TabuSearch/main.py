#!/usr/bin/python3
import sys
from TS import runTabuSearch

if(len(sys.argv) < 5):
    print("Usage: python3 main.py <data> <nTests> <nNeighbors> <seed>")
    exit()

path = sys.argv[1]
nTests = int(sys.argv[2])
nNeighbors = int(sys.argv[3])
seed = int(sys.argv[4])

print("Running Tabu Search for '{}'".format(path))

runTabuSearch(path, nTests, nNeighbors, seed)
