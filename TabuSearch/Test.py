import random
import TS
from ReadInstance import ReadInstance
from ModellingProblem import Solution

nDepots, nTrips, maxBus, depotToTrip, tripToDepot, tripToTrip = ReadInstance("./TabuSearch/instances-inp/m4n500s2.inp")
#print(nDepots)
#print(nTrips)
#print(maxBus)
#print(depotToTrip)
#print(tripToTrip)
#print(tripToDepot)

random.seed(5643879)

for i in range(1):
    try:
        test = Solution(nDepots, nTrips, maxBus, depotToTrip, tripToDepot, tripToTrip)
        test.generateConstructiveSolution()
        test.getNeighbor([])

        print(test.value)
        print(test.getNumOfBus())
    except Exception:
        test = None

