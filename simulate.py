import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time 
import numpy as np

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

# Make a plane for objects to rest on, world for objects, body of robot
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")
robot = p.loadURDF("body.urdf")
NB_LOOPS = 500
backLegSensorValues = np.zeros(NB_LOOPS)
frontLegSensorValues = np.zeros(NB_LOOPS)
pyrosim.Prepare_To_Simulate(robot)
for i in range(NB_LOOPS):
    p.stepSimulation()

    # sensorize
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    # # motorize
    # pyrosim.Set_Motor_For_Joint(
    # bodyIndex = robot,
    # jointName = "Torso_BackLeg",
    # controlMode = p.POSITION_CONTROL,
    # targetPosition = 0.0,
    # maxForce = 500) #(in Newton-metres)
    
    # pyrosim.Set_Motor_For_Joint(
    # bodyIndex = robot,
    # jointName = "Torso_FrontLeg",
    # controlMode = p.POSITION_CONTROL,
    # targetPosition = 0.0,
    # maxForce = 500) #(in Newton-metres)
    

    time.sleep(0.01)
    #print(i)
p.disconnect()

#sensor outputs
np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues", frontLegSensorValues)