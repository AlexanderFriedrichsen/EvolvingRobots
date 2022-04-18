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


#change this for now for testing purposes to 1
numberOfGenerations = 5
populationSize = 10

#before hex: 9 and 8
numSensorNeurons = 9
numMotorNeurons  = 8

#hexapod
numberLegs = 6

motorJointRange = .3