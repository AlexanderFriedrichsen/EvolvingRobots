import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time 
import numpy as np
# import sys
# print(sys.version)

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

# Make a plane for objects to rest on, world for objects, body of robot
planeId = p.loadURDF("plane.urdf")
worldId = p.loadSDF("world.sdf")
robotId = p.loadURDF("body.urdf")

backLegSensorValues = np.zeros(500)
frontLegSensorValues = np.zeros(500)
pyrosim.Prepare_To_Simulate(robotId)
for i in range(500):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    time.sleep(0.01)
    print(i)
p.disconnect()

#sensor outputs
np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues", frontLegSensorValues)