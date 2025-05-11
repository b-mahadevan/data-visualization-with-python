from random_walks import RandomWalk

from matplotlib import pyplot as plt


plot = 1

while True:

    #Initializing the class
    rw = RandomWalk(50000)
    rw.fill_walks()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 8), dpi = 128)

    points = range(rw.num_points)

    #Scatter plot using colormap
    ax.scatter(rw.x_values, rw.y_values, c=points, cmap=plt.cm.Blues, edgecolors='none', s=1)
    ax.scatter(0, 0, c='green', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)
    
    ax.set_aspect('equal')

    #Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    #Save the plot into a file
    filename = f'output{plot}'
    plt.savefig(filename, bbox_inches = 'tight')
    print(f'Succesffully saved the output {plot}')

    another_walk = input('Want another walk: (y/n)')

    plot += 1

    if another_walk == 'n':
        break

