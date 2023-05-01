import numpy as np

# simulation gravity
DEFAULT_GRAVITY = -9.8

# How long the simulation should run for
LOOP_LENGTH = 1000

PI = np.pi
# Leg Forces
AMPLITUDE = PI/4.0
FREQUENCY = 20
PHASE_OFFSET = 0

targetAngles = np.linspace(-np.pi, np.pi, LOOP_LENGTH)
LEG_MOTOR_MAX_FORCE = 20

# time sleep rate
SLEEP_RATE = 1/480 

numberOfGenerations = 100
populationSize = 10

motorJointRange = .3

numberLegs = 4

#before hex: 8 and 9
# we are making our code modular to the number of legs.
# the number sensor neurons is the number of legs * 2, and motors is *2 +1
numSensorNeurons = numberLegs * 2
numMotorNeurons  = (numberLegs * 2) + 1


