# from solution_hex import SOLUTION_HEX
from solution import SOLUTION
import constants as c
import copy
import os
import numpy as np

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system('del brain*.nndf')
        os.system('del fitness*.nndf')
        os.system('w fitness**.nndf')
        self.nextAvailableID = 0
        self.parents = {}

        #p population # columns, g generation # rows
        self.fitnessMatrix = np.zeros((c.populationSize, c.numberOfGenerations))

        #self.children = {}
        for i in range(c.populationSize):
            # self.parents[i] = SOLUTION_HEX(self.nextAvailableID)
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        # moved
        self.parents[0].Create_World()
        self.parents[0].Generate_Body()


    def Evolve(self):
        # self.parent.Evaluate("GUI")
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            
            for p in range(c.populationSize):
                individualFitness = self.parents.get(p).fitness
                self.fitnessMatrix.itemset((p, currentGeneration), individualFitness)


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()


    def Spawn(self):
        self.children = {}
        for s in range(len(self.parents)):
            self.parents[s].Set_ID()
            self.children[s] = copy.deepcopy(self.parents[s])
            self.nextAvailableID += 1

    def Mutate(self):
        for child in range(len(self.children)):
            self.children[child].Mutate()

    def Select(self):
        for key in range(len(self.parents)):
            if self.parents[key].fitness < self.children[key].fitness:
                self.parents[key] = self.children[key]

    def Print(self):
        print('\n')
        for key in range(len(self.parents)):
            print('Parent:', self.parents[key].fitness, '<', 'Child:', self.children[key].fitness)
        print('\n')

    def Show_Best(self):
        bestkey = 0
        bestFit = self.parents[0].fitness
        for key in range(len(self.parents)):
            if self.parents[key].fitness < bestFit:
                bestFit = self.parents[key].fitness
                bestkey = key
        self.parents[bestkey].Start_Simulation("GUI")


    def Evaluate(self, solutions):
        for s in range(len(solutions)):
            solutions[s].Start_Simulation("DIRECT")
        for s in range(len(solutions)):
            solutions[s].Wait_For_Simulation_To_End()

    def Fitness(self):
        #add the current gen and pop # to the correct row-col in the matrix
        pass
        

    def SaveFitness(self):
        np.savetxt("data/fitnessMatrix" + str(c.numberLegs) + ".txt", self.fitnessMatrix)
        np.save("data/fitnessMatrix" + str(c.numberLegs) +".npy", self.fitnessMatrix)
