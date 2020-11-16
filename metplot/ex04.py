from matplotlib import pyplot as plt
import numpy as np
from numpy.random import randn

fig = plt.figure()

splt1 = fig.add_subplot(2, 2, 1)
splt1.plot([2, 4, 5, 6], [81, 93, 91, 97])

sp1 = fig.add_subplot(2, 2, 2)
sp1.plot(randn(50).cumsum(), 'k--')

sp2 = fig.add_subplot(2, 2, 3)
sp2.hist(randn(100),bins=20, color='r', alpha=0.3)

sp3 = fig.add_subplot(2, 2, 4)
sp3.scatter(np.arange(100),np.arange(100)+3*randn(100))

plt.show()