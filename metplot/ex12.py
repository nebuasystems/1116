from matplotlib import pyplot as plt
import numpy as np
from numpy.random import randn

fig, sp = plt.subplots(1, 1)

sp.plot([1, 2, 3, 4], [10, 20, 30, 40], color='#f0f', lineStyle='-.', marker='v')


plt.show()
