import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time 
import numpy as np
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

# Make a plane for objects to rest on, world for objects, body of robot
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")
robot = p.loadURDF("body.urdf")
NB_LOOPS = 2000
backLegSensorValues = np.zeros(NB_LOOPS)
frontLegSensorValues = np.zeros(NB_LOOPS)

FrontLeg_amplitude = np.pi/4.0
FrontLeg_frequency = 20
FrontLeg_phaseOffset = 0

BackLeg_amplitude = np.pi/4.0
BackLeg_frequency = 20
BackLeg_phaseOffset = np.pi/4

targetAngles = np.linspace(-np.pi/4, np.pi/4, NB_LOOPS)
FrontLeg_motorCommand = FrontLeg_amplitude * np.sin(FrontLeg_frequency * targetAngles + FrontLeg_phaseOffset)
BackLeg_motorCommand = BackLeg_amplitude * np.sin(BackLeg_frequency * targetAngles + BackLeg_phaseOffset)


pyrosim.Prepare_To_Simulate(robot)
for i in range(NB_LOOPS):
    p.stepSimulation()

    # sensorize
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")



    # motorize Torso_BackLeg
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robot,
    jointName = "Torso_BackLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition = BackLeg_motorCommand[i],
    maxForce = 20) #(in Newton-metres)
    
    # motorize Torso_FrontLeg
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robot,
    jointName = "Torso_FrontLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition = FrontLeg_motorCommand[i],
    maxForce = 20) #(in Newton-metres)
    
    # pyrosim.Set_Motor_For_Joint(
    # bodyIndex = robot,
    # jointName = "Torso_FrontLeg",
    # controlMode = p.POSITION_CONTROL,
    # targetPosition = 0.0,
    # maxForce = 500) #(in Newton-metres)
    

    time.sleep(1/240)
    #print(i)
p.disconnect()

#sensor outputs
np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues", frontLegSensorValues)
np.save('data/targetAngles.npy',targetAngles)
np.save('data/BackLeg_motorCommand.npy',BackLeg_motorCommand)
np.save('data/FrontLeg_motorCommand.npy',FrontLeg_motorCommand)
exit()