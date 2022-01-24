import pybullet as p
import pybullet_data
import time 
# import sys
# print(sys.version)



physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

# Make a plane for objeccts to rest on
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")
robotID = p.loadURDF("body.urdf")
for i in range(10000):
    p.stepSimulation()
    time.sleep(0.01)
    print(i)
p.disconnect()
