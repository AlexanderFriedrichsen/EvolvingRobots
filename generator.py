import pyrosim.pyrosim as pyrosim


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    # size
    length = 1
    height = 1
    width = 1
    # position  - a link start with its exact center at these cords.
    x = -2
    y = 2
    z = .5
    # when starting same position, why did it go x and not y?
    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])

    pyrosim.End()

def Create_Robot():
    # torso size
    torsoLength = 1
    torsoHeight = 1
    torsoWidth = 1
    # position  - a link start with its exact center at these cords.
    x = 0
    y = 0
    z = 1.5
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[x,y,z] , size=[torsoLength,torsoWidth,torsoHeight])
    
    # legs size
    legLength = 1
    legHeight = 1
    legWidth = 1

    #create BackLeg
    pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-.5,1])
    pyrosim.Send_Cube(name="BackLeg", pos=[0,-.5,-.5] , size=[legLength,legWidth,legHeight])
    
    #create FrontLeg
    pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,.5,1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0,.5,-.5] , size=[legLength,legWidth,legHeight])
   

    
    pyrosim.End()

if __name__ == '__main__':
    Create_World()
    Create_Robot()
