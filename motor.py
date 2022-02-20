import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    
    def __init__(self, jointName):
        self.jointName = jointName
       # self.joints = {}
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.motorValues = np.zeros(c.NB_LOOPS)
        self.amplitude = c.AMPLITUDE
        self.frequency = c.FREQUENCY
        self.offset = c.PHASE_OFFSET

        if self.jointName == "Torso_BackLeg":
            self.frequency *= 2
        for i in range(c.NB_LOOPS):
            self.motorValues[i] = self.amplitude * np.sin(self.frequency * c.targetAngles[i] + self.offset)

    def Set_Value(self, robot, t):
        pyrosim.Set_Motor_For_Joint(

            bodyIndex=robot,

            jointName= self.jointName,

            controlMode=p.POSITION_CONTROL,

            targetPosition=self.motorValues[t],

            maxForce=20
        )

    def Save_Values(self):
        np.save('data//motorValues.npy', self.motorValues)
