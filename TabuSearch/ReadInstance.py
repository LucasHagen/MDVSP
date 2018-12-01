import numpy as np

def ReadInstance(fileName: str):
    with open(fileName, "r") as fileInstance:
        rawText = fileInstance.readlines()

    # First line: d = number of depots, t = number of trips, ld = d values, maxbus
    firstLine = [int(x) for x in rawText[0].split("\t")]
    nDepots = firstLine[0]
    nTrips = firstLine[1]
    maxBus = firstLine[2:]
    rawText.pop(0)

    depotToTrip = np.ndarray(shape = (nDepots, nTrips))
    
    for d in range(nDepots):
    
        dToT = [ x for x in rawText[0].split("\t")[nDepots:-1] ] #-1 defines that we will remove the \n at the end of every list
        for i in range(len(dToT)):
            depotToTrip[d][i] = dToT[i]
        rawText.pop(0)
    
    tripToDepot = np.ndarray(shape = (nTrips, nDepots))
    tripToTrip = np.ndarray(shape = (nTrips, nTrips))

    for t in range(nTrips):
    
        tToD = [ x for x in rawText[0].split("\t")[:nDepots] ]
        for i in range(len(tToD)):
            tripToDepot[t][i] = tToD[i]
    
        tToT = [ x for x in rawText[0].split("\t")[nDepots:-1] ]
        for i in range(len(tToT)):
            tripToTrip[t][i] = tToT[i]
    
        rawText.pop(0)
    
    
    if(rawText != []):
        raise Exception("Not a valid instance: first line probably has wrong info.")
    return(nDepots, nTrips, maxBus, depotToTrip, tripToDepot, tripToTrip)

