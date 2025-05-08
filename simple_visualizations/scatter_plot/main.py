from matplotlib import pyplot as plt

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots(figsize=(7,5))

x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y_values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

ax.scatter(x_values, y_values, s=100)

ax.set_title('Fibonacci Sequence Scatter Plot', fontsize=25)

ax.set_xlabel('Index (n)', fontsize=15)
ax.set_ylabel('Fibonacci Numbers F(n)',fontsize=15)

ax.tick_params(labelsize=14)

plt.show()