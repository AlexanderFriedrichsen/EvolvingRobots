from world import WORLD
from robot import ROBOT
import constants as c
import pybullet as p
import pybullet_data
import time

class SIMULATION:

    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.EARTH_GRAVITY)

        self.world = WORLD()
        self.robot = ROBOT()
       
    def Run(self):
        for i in range(c.NB_LOOPS):
            p.stepSimulation()

            self.robot.Sense(i)
            self.robot.Act(i)

            time.sleep(c.SLEEP_RATE)
            print(i)

    def __del__(self):
        p.disconnect()


        