from matplotlib import pyplot as plt

input_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

fig, ax = plt.subplots(figsize = (7, 5))

ax.plot(input_values, fibonacci_sequence, linewidth = 3)

ax.set_title('Fibonacci Sequence Plot', fontsize=25)
ax.set_xlabel('Index (n)', fontsize=15)
ax.set_ylabel('Fibonacci Number F(n)', fontsize=15)

ax.tick_params(labelsize=14)

plt.show()