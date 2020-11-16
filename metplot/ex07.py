from matplotlib import pyplot as plt
import numpy as np
from numpy.random import randn

fig, splts = plt.subplots(2, 2, sharex=True, sharey=True)

for i in range(2):
    for j in range(2):
        splts[i, j].hist(randn(100), color='k', alpha=0.3)

plt.subplots_adjust(wspace=0, hspace=0)

plt.show()

