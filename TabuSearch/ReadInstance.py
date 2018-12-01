
def ReadInstance(fileName):
    with open(fileName, "r") as fileInstance:
        rawText = fileInstance.readlines()

    # First line: d = number of depots, t = number of trips, ld = d values, maxbus
    firstLine = [int(x) for x in rawText[0].split("\t")]
    nDepots = firstLine[0]
    nTrips = firstLine[1]
    maxBus = firstLine[2:]
    rawText.pop(0)

    depotToTrip = {}
    for d in range(nDepots):
        depotToTrip[d] = [ x for x in rawText[0].split("\t")[nDepots:-1] ] #-1 defines that we will remove the \n at the end of every list
        rawText.pop(0)
    
    tripToDepot = {}
    tripToTrip = {}
    for t in range(nTrips):
        tripToDepot[t] = [ x for x in rawText[0].split("\t")[:nDepots] ]
        tripToTrip[t] = [ x for x in rawText[0].split("\t")[nDepots:-1] ]
        rawText.pop(0)
    if(rawText != []):
        raise Exception("Not a valid instance: first line probably has wrong info.")
    return(nDepots, nTrips, maxBus, depotToTrip, tripToDepot, tripToTrip)

