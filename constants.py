import numpy as np

#store constants for simulate.py

NB_LOOPS = 2000
SLEEP_RATE = 1/240
EARTH_GRAVITY = -9.8

AMPLITUDE = np.pi/4.0
FREQUENCY = 20
PHASE_OFFSET = 0

NUMBER_OF_GENERATIONS = 20

targetAngles = np.linspace(-np.pi/4, np.pi/4, NB_LOOPS)

populationSize = 10