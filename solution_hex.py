import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constants as c

class SOLUTION_HEX:
    def __init__(self, myID):
        self.myID = myID
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        self.weights = self.weights * 2 -1

    def Evaluate(self, directOrGUI):
        pass

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        #pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
        pyrosim.Send_Sphere(name="BowlingBall" , pos=[-3,+3,0.5] , size=[0.5])
        pyrosim.End()

    def Generate_Body(self):
        # Create Robot
        # here is where we will be adding 2 limbs. Do we want to reposition the other limbs as well? Perhaps, but not initially

        pyrosim.Start_URDF("body.urdf")
        length = 1
        width = 1
        height = 1
        x = 0
        y = 0
        z = 1
        # Add Torso
        pyrosim.Send_Cube(name="Torso", pos=[x, y, z], size=[length, width, height])

        # Create Legs
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, .5, 0], size=[0.2, 1, 0.2])
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -.5, 0], size=[0.2, 1, 0.2])
        pyrosim.Send_Cube(name="LeftLeg", pos=[-.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])

        #let's try displacing by .4 on either side of the middle front leg
        #this might need to be reversed?
        #pyrosim.Send_Cube(name="frontLeftLeg", pos=[0, .5, .4], size=[0.2, 1, 0.2])
        #pyrosim.Send_Cube(name="frontRightLeg", pos=[0, .5, -.4], size=[0.2, 1, 0.2])
        
        # Create Lower Legs
        pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0, 0, -.5], size=[.2, .2, 1])
        pyrosim.Send_Cube(name="LowerBackLeg", pos=[0, 0, -.5], size=[.2, .2, 1])
        pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0, 0, -.5], size=[.2, .2, 1])
        pyrosim.Send_Cube(name="LowerRightLeg", pos=[0, 0, -.5], size=[.2, .2, 1]) 
        
        #We also need to add lower parts for the front legs - it seems like they can all remain the same
        #pyrosim.Send_Cube(name="LowerFrontLeftLeg", pos=[0, 0, -.5], size=[.2, .2, 1])
        #pyrosim.Send_Cube(name="LowerFrontRightLeg", pos=[0, 0, -.5], size=[.2, .2, 1])

        # Create Joints Upper
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",type="revolute", position="0 0.5 1", jointAxis = "1 0 0")
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg",type="revolute", position="0 -0.5 1", jointAxis = "1 0 0")
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg",type="revolute", position="-0.5 0 1", jointAxis = "0 1 0")
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg",type="revolute", position="0.5 0 1", jointAxis = "0 1 0")

        #Also adding joints... what should the position be?
        #pyrosim.Send_Joint(name="Torso_FrontLeftLeg", parent="Torso", child="FrontLeftLeg",type="revolute", position="0 0.5 1", jointAxis = "1 0 0")
        #pyrosim.Send_Joint(name="Torso_FrontRightLeg", parent="Torso", child="FrontRightLeg",type="revolute", position="0 0.5 1", jointAxis = "1 0 0")

        # Create Joints Lower
        pyrosim.Send_Joint(name="FrontLeg_LowerFrontLeg", parent="FrontLeg", child="LowerFrontLeg",type="revolute", position="0 1 0", jointAxis = "1 0 0")
        pyrosim.Send_Joint(name="BackLeg_LowerBackLeg", parent="BackLeg", child="LowerBackLeg",type="revolute", position="0 -1 0", jointAxis = "1 0 0")
        pyrosim.Send_Joint(name="LeftLeg_LowerLeftLeg", parent="LeftLeg", child="LowerLeftLeg",type="revolute", position="-1 0 0", jointAxis = "0 1 0")
        pyrosim.Send_Joint(name="RightLeg_LowerRightLeg", parent="RightLeg", child="LowerRightLeg", type="revolute", position="1 0 0", jointAxis = "0 1 0")
   
        # ok finally we need to add lower joints.. positions need to be tested as well
        #pyrosim.Send_Joint(name="FrontLeftLeg_LowerFrontLeftLeg", parent="FrontLeftLeg", child="LowerFrontLeftLeg",type="revolute", position="0 1 0", jointAxis = "1 0 0")
        #pyrosim.Send_Joint(name="FrontRightLeg_LowerFrontRightLeg", parent="FrontRightLeg", child="LowerFrontRightLeg",type="revolute", position="0 1 0", jointAxis = "1 0 0")
        pyrosim.End()

    def Generate_Brain(self):
        # Create World
        #in total we add 4 more to each of sensor and motor neurons with the extra 2 legs. Reindex
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="FrontLeftLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="FrontRightLeg")
                
        pyrosim.Send_Sensor_Neuron(name=7, linkName="LowerFrontLeg")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="LowerBackLeg")
        pyrosim.Send_Sensor_Neuron(name=9, linkName="LowerLeftLeg")
        pyrosim.Send_Sensor_Neuron(name=10, linkName="LowerRightLeg")
        pyrosim.Send_Sensor_Neuron(name=11, linkName="LowerFrontLeftLeg")
        pyrosim.Send_Sensor_Neuron(name=12, linkName="LowerFrontRightLeg")
        
        pyrosim.Send_Motor_Neuron(name=13, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=14, jointName="Torso_BackLeg")   
        pyrosim.Send_Motor_Neuron(name=15, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=16, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=17, jointName="Torso_FrontLeftLeg")
        pyrosim.Send_Motor_Neuron(name=18, jointName="Torso_FrontRightLeg")
                
        pyrosim.Send_Motor_Neuron(name=19, jointName="FrontLeg_LowerFrontLeg")
        pyrosim.Send_Motor_Neuron(name=20, jointName="BackLeg_LowerBackLeg")   
        pyrosim.Send_Motor_Neuron(name=21, jointName="LeftLeg_LowerLeftLeg")
        pyrosim.Send_Motor_Neuron(name=22, jointName="RightLeg_LowerRightLeg")
        pyrosim.Send_Motor_Neuron(name=23, jointName="FrontLeg_LowerFrontLeftLeg")
        pyrosim.Send_Motor_Neuron(name=24, jointName="FrontLeg_LowerFrontRightLeg")


        # loop over the names
        for currentRow in range(c.numSensorNeurons):
            # loop over the motors
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,
                                     targetNeuronName=currentColumn + c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])
        
        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons -1)
        randomColumn = random.randint(0, c.numMotorNeurons-1)
        self.weights[randomRow,randomColumn] = random.random() * 2 -1

    def Set_ID(self):
        self.myID

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myID))


    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)
        fitnessFile = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()
        os.system('del fitness' + str(self.myID) +'.txt')