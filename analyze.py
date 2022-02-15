import numpy as np
import matplotlib.pyplot as pyplot


#one argument is treated as a set of y values
# pyplot.plot(backLegSensorValues, label="back", linewidth=2)
# pyplot.plot(frontLegSensorValues, label="front")
# pyplot.legend()
# pyplot.show()

# backLegSensorValues = np.load('data/backLegSensorValues.npy')
# back = pyplot.plot(backLegSensorValues,linewidth=2, label='backLegSensorValues')
# pyplot.legend()


# frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
# front = pyplot.plot(frontLegSensorValues, color='red',linewidth=2, label='frontLegSensorValues')
# pyplot.legend()
# pyplot.show()

TargetAngles = np.load('data/targetAngles.npy')
front = pyplot.plot(TargetAngles, color='pink',linewidth=5, label='targetAngles')
pyplot.legend()
pyplot.show()

BackLeg_motorCommand = np.load('data/BackLeg_motorCommand.npy')
front = pyplot.plot(BackLeg_motorCommand, color='green',linewidth=5, label='Back Motor values')
pyplot.legend()

FrontLeg_motorCommand = np.load('data/FrontLeg_motorCommand.npy')
front = pyplot.plot(FrontLeg_motorCommand, color='yellow',linewidth=5, label='Front Motor values')
pyplot.legend()
pyplot.show()

