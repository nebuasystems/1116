from matplotlib import pyplot as plt

fig = plt.figure()
splt1 = fig.add_subplot(2, 1, 1)
splt1.plot([2, 3, 5, 6], [81, 93, 91, 97])


splt2 = fig.add_subplot(2, 1, 2)
splt2.plot([2, 3, 5, 6], [81, 93, 91, 97])

plt.show()