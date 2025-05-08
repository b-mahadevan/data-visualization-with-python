from matplotlib import pyplot as plt

fibbonacci_series = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

fig, ax = plt.subplots()

ax.plot(fibbonacci_series)

plt.show()