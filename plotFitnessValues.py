import constants as c
import os
import matplotlib.pyplot as plt
import numpy as np


quadValues = np.load('data/fitnessMatrix4.npy')
#quad = matplotlib.pyplot.plot(quadValues[0,:],linewidth=2, label='Quadaped Fitness Values')
#matplotlib.pyplot.legend()

hexValues = np.load('data/fitnessMatrix6.npy')
octoValues = np.load('data/fitnessMatrix8.npy')

quadCollapsed = np.zeros(c.numberOfGenerations)
hexCollapsed = np.zeros(c.numberOfGenerations)
octoCollapsed = np.zeros(c.numberOfGenerations)
quad_std = np.zeros(c.numberOfGenerations)
hex_std = np.zeros(c.numberOfGenerations)
octo_std = np.zeros(c.numberOfGenerations)


for g in range(c.numberOfGenerations):
    quadCollapsed[g] = np.mean(quadValues[:, g])
    quad_std[g] = np.std(quadValues[g])

    hexCollapsed[g] = np.mean(hexValues[:, g])
    hex_std[g] = np.std(hexValues[g])

    octoCollapsed[g] = np.mean(octoValues[:, g])
    octo_std[g] = np.std(octoValues[g])
print(quadCollapsed)
print(quad_std)

#print(hexCollapsed)
#print(octoCollapsed)


quad = plt.plot(quadCollapsed, linewidth=2, label='Quadraped Fitness Values', color = 'green')
quad_std_plus = plt.plot(quadCollapsed+quad_std, linewidth=2, label='Quadraped SD Values', color = 'green')
quad_std_minus = plt.plot(quadCollapsed-quad_std, linewidth=2, label='Quadraped SD Values', color = 'green')

hex = plt.plot(hexCollapsed, linewidth=2, label='Hexapod Fitness Values', color = 'purple')
hex_std_plus = plt.plot(hexCollapsed+hex_std, linewidth=2, label='hexapod SD + Values', color = 'purple')
hex_std_minus = plt.plot(hexCollapsed-hex_std, linewidth=2, label='hexapod SD - Values', color = 'purple')

octo = plt.plot(octoCollapsed, linewidth=2, label='Octopod Fitness Values', color = 'magenta')
octo_std_plus = plt.plot(octoCollapsed+octo_std, linewidth=2, label='octopod SD + Values', color = 'magenta')
octo_std_minus = plt.plot(octoCollapsed-octo_std, linewidth=2, label='octopod SD - Values', color = 'magenta')

plt.ylabel('Fitness')
plt.xlabel('Generation')
plt.title('A/B test Body Building')
plt.legend()
plt.savefig("data/fitnessValues1")
plt.show()
