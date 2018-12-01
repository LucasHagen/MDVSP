import numpy as np

class Solution():
    def __init__(self, nDepots, nTrips):
        self.nDepots = nDepots
        self.nTrips = nTrips
        self.solutionMatrix = np.zeros(shape = (nDepots, nTrips), dtype=int) #Represents if a bus is going out of the depot to a trip. Initially has only zeros, and has binary values


    def generateRandomSolution(self, seedSolution):
        pass
    

    