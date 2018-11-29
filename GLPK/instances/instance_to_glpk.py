#!/usr/bin/python
import sys

if len(sys.argv) < 3:
    print("Usage: python3 instance_to_glpk.py <input file> <output file>")
    exit()

inputPath  = sys.argv[1]
outputPath = sys.argv[2]

print("Instance Converter Started...")
print("[0] Opening '{}'".format(inputPath))

input = open(inputPath)

print("[1] Reading Format File")

formatFile = open("model.data")
outputData = formatFile.read()
formatFile.close()

print("[2] Converting Data")

firstLine = input.readline().split("\t")
nDepots   = int(firstLine[0])
nTrips    = int(firstLine[1])
depots    = ""
trips     = ""
maxBus    = ""
mheader   = ""
mlines    = ""

for i in range(nDepots):
    d       =  "D{} ".format(i)
    mheader += d
    depots  += d
    maxBus  += "\nD{}  {} ".format(i, firstLine[i + 2].replace('\n', ''))
for i in range(nTrips):
    t       =  "T{} ".format(i)
    mheader += t
    trips   += t

for i in range(nDepots):
    mlines += "D{} {}\n".format(i, input.readline().replace('\t', ' ').replace('\n', ''))
for i in range(nTrips):
    mlines += "T{} {}\n".format(i, input.readline().replace('\t', ' ').replace('\n', ''))

outputData = outputData.format(depots = depots, trips = trips, maxbus = maxBus, mheader = mheader, mlines = mlines)

input.close()

print("[3] Opening '{}'".format(outputPath))

output = open(outputPath, 'w')

print("[4] Writting to '{}'".format(outputPath))

output.write(outputData)
output.close()

print(" - Done! '{}' -> '{}'".format(inputPath, outputPath))
