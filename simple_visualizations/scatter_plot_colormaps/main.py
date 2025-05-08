from matplotlib import pyplot as plt

x_values = range(1, 1001)

y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots(figsize=(7,5))

ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.twilight, s=10)

ax.set_title('Square Numbers Plot', fontsize=25)

ax.set_xlabel('Value', fontsize=15)
ax.set_ylabel('Square Value',fontsize=15)

ax.tick_params(labelsize=14)

plt.show()