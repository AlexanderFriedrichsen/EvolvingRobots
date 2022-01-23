import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
# size
length = 1
height = 1
width = 1

# position  - a link start with its exact center at these cords.
x = 0
y = 0
z = .5

x2 = 1
y2 = 0
z2 = 1.5
# when starting same position, why did it go x and not y?
#pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
#pyrosim.Send_Cube(name="Box2", pos=[x2,y2,z2] , size=[length,width,height])

# towers:
for m in range(6):
    for n in range(6):
        for i in range(6):
            pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
            z+=1
            length *= .9 
            height *= .9 
            width *= .9

        z=.5
        x+=1
        length = 1
        width = 1
        height = 1
    y+=1
    x=0



pyrosim.End()