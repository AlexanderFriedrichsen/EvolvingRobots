import numpy as np
import pyrosim.pyrosim as pyrosim
import os

class SOLUTION:
    def __init__(self):
        self.weights = 2 * np.random.rand(3,2) - 1

    def Evaluate(self, mode):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        os.system("python simulate.py " + mode)


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        # size
        length = 1
        height = 1
        width = 1
        # position  - a link start with its exact center at these cords.
        x = -3
        y = 3
        z = .5
        
        pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])

        pyrosim.End()

    def Create_Body(self):
        # torso size
        torsoLength = 1
        torsoHeight = 1
        torsoWidth = 1
        # position  - a link start with its exact center at these cords.
        x = 0
        y = 0
        z = 0.5
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[x,y,z+1] , size=[torsoLength,torsoWidth,torsoHeight])
        
        # legs size
        legLength = 1
        legHeight = 1
        legWidth = 1

        #create BackLeg
        pyrosim.Send_Joint(name="Torso_BackLeg" , parent="Torso", child="BackLeg",
                        type = "revolute", position =[.5,0,1])#".5 0 1") # 
        pyrosim.Send_Cube(name="BackLeg", pos=[0.5,0,-.5] , size=[legLength, legWidth, legHeight])
        
        #create FrontLeg
        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg", 
                        type = "revolute", position = [-.5,0,1]) #"-.5 0 1") # 
        pyrosim.Send_Cube(name="FrontLeg", pos=[-.5,0,-.5] , size=[legLength,legWidth,legHeight])
        pyrosim.End()


    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

        pyrosim.Send_Synapse(sourceNeuronName = 0, targetNeuronName = 3, weight = -1.0)
        pyrosim.Send_Synapse(sourceNeuronName = 1, targetNeuronName = 3, weight = -1.0)
        pyrosim.Send_Synapse(sourceNeuronName = 0, targetNeuronName = 4, weight = -1.0)
        pyrosim.Send_Synapse(sourceNeuronName = 1, targetNeuronName = 4, weight = -1.0)

        # loop over the names of the neurons
        for currentRow in range(3):
            # loop over the motors
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=self.weights[currentRow][currentColumn])


        pyrosim.End()