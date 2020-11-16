from matplotlib import pyplot as plt
import numpy as np
from numpy.random import randn

fig, sp = plt.subplots()

sp.plot(randn(1000).cumsum())
sp.set_xticks([0, 100, 200, 800, 900])
sp.set_xticklabels(['a', 'v', 'v', 'v', 'v'], fontsize='small')


plt.xlabel('plt yl')
sp.set_xlabel('xl')
plt.ylabel('yl')
plt.show()
