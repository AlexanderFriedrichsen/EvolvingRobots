import numpy as np
import matplotlib.pyplot as pyplot

backLegSensorValues = np.load("data/backLegSensorValues.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")

#one argument is treated as a set of y values
pyplot.plot(backLegSensorValues, label="back", linewidth=2)
pyplot.plot(frontLegSensorValues, label="front")

pyplot.legend()
pyplot.show()