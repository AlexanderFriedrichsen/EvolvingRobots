Repository for my Evolutionary Robotics Class

Here is where I ill keep notes on how to work with the code:

Pybullet Physics:
- applying forces to each link in the world,
- updating its acceleration based on the forces that are acting on it using f = ma, and
- updating the new position and orientation of each link using its new acceleration.

joints and links:
- Only the first joint in a robot has an absolute position. Each other joint hasa position relative to its upstream joint.

Body building final project:

We have implemented:
- spheres
- modular number of legs
- (implied) modular number of neurons

Next, we attempt to gather data between quadruped / hexapod / octopod gaits and see which gait achieves the maximum displacement.

We will gather the fitness values after multiple runs of each.
Each run we will record the fitness value of the best performing child after 5 generations for a population of size 50


