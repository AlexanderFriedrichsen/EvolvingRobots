from world import WORLD
from robot import ROBOT
import constants as c
import pybullet as p
import pybullet_data
import time


class SIMULATION:

    def __init__(self, mode):
        self.directOrGUI = mode
        if mode == 'GUI':
            p.connect(p.GUI)
        else:
            p.connect(p.DIRECT)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        
        p.setGravity(0, 0, c.EARTH_GRAVITY)

        self.world = WORLD()
        self.robot = ROBOT()
       
    def Run(self):
        for i in range(c.NB_LOOPS):
            p.stepSimulation()

            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

            if self.directOrGUI == 'GUI':
                time.sleep(c.SLEEP_RATE)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()


        