from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import pybullet_data

class ROBOT:
    
    def __init__(self):
        self.robot = p.loadURDF("body.urdf")
        self.sensors = {}
        self.motors = {}
        self.values = {}
        pyrosim.Prepare_To_Simulate(self.robot)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
    
    def Prepare_To_Sense(self):

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for key in self.sensors:
            self.values[t] = self.sensors[key].Get_Value(t)
            if t == c.NB_LOOPS:
                print(self.sensors[key])

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            print(jointName)
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for key in self.motors:
            print(self.motors)
            print(key)
            self.motors[key].Set_Value(self.robot, t)
            #if t == c.LOOP_LENGTH:
            print(self.motors[key])
    
    def Save_Values(self):
        for key in self.motors:
            self.motors[key].Save_Values()
        for key in self.sensors:
            self.sensors[key].Save_Values()