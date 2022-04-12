Repository for my Evolutionary Robotics Class

Here is where I ill keep notes on how to work with the code:

Pybullet Physics:
- applying forces to each link in the world,
- updating its acceleration based on the forces that are acting on it using f = ma, and
- updating the new position and orientation of each link using its new acceleration.

joints and links:
- Only the first joint in a robot has an absolute position. Each other joint hasa position relative to its upstream joint.

The code for the base of the final is based on a previous evolutionary robotics repository 
that organized the codebase better than I did up until this point. It is however the same functionality as my code for the quadruped,
and I will be building on it on my own from now on.

I am going to implement a multi-objective optimization method.

This week I began reading the Pymoo documentation to get up to speed on multi-optimization algorithms, python implementation, 
and how to format a multi-optimization problem. In our case, we want to optimize the speed of the robot, and I've chosen the second 
optimization to be a function of least time touching the ground with limbs. Thus, we are left with a model as follows:

Optimization Problem Definition:

minimize -f_m(x_i) where m = 1, 2 as we have two functions to optimize. The function is negative because we are maximizing, but we are in the mindset of minimizing.
These functions are f_1(x) and f_2(x) pertaining to displacement and time off ground respectively.
We also have our inequality constraints, g_j(x) <= 0, which ensure that the robot is optimized for a minimum threshold of speed and time off ground.

x_i represents the variables to be optimized, with lower and upper bounds on each x.

I read through the getting started guide on Pymoo:  have also started the definition for our specific problem above
I am interested to know if my second chosen optimization function is the easiest to implement, as I forsee the implementation already being quite tricky.
I am looking for feedback anad will reach out as per recommendation for this project choice this week.

