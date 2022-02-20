import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim
class SENSOR:
    
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.NB_LOOPS)
    
    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        return self.values

    def Save_Values(self):
        np.save('data//sensorValues.npy', self.values)