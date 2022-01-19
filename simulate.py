import pybullet as p
import time 
# import sys
# print(sys.version)



physicsClient = p.connect(p.GUI)

for i in range(1000):
    p.stepSimulation()
    time.sleep(0.02)
    print(i)
p.disconnect()
