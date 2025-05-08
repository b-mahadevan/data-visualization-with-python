from matplotlib import pyplot as plt

fibbonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

fig, ax = plt.subplots()

ax.plot(fibbonacci_sequence)

plt.savefig('output.png', bbox_inches = 'tight')