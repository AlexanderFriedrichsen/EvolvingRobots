import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time 
# import sys
# print(sys.version)



physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

# Make a plane for objeccts to rest on
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")
robotId = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robotId)
for i in range(10000):
    p.stepSimulation()
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    time.sleep(0.01)
    print(i)
p.disconnect()
