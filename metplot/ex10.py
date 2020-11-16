from matplotlib import pyplot as plt
import numpy as np
from numpy.random import randn

fig, sp = plt.subplots(1, 1)

sp.plot([10, 20, 30, 40], label='data1')
sp.plot([9, 15, 21, 35], label='data2')

plt.legend(loc='best')

plt.show()
