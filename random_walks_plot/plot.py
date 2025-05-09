from random_walks import RandomWalk

from matplotlib import pyplot as plt


plot = 1

while True:

    #Initializing the class
    rw = RandomWalk()
    rw.fill_walks()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 12))

    points = range(rw.num_points)

    #Scatter plot using colormap
    ax.scatter(rw.x_values, rw.y_values, c=points, cmap=plt.cm.Blues, edgecolors='none', s=15)
    
    ax.set_aspect('equal')

    #Save the plot into a file
    filename = f'output{plot}'
    plt.savefig(filename, bbox_inches = 'tight')
    print(f'Succesffully saved the output {plot}')

    another_walk = input('Want another walk: (y/n)')

    plot += 1

    if another_walk == 'n':
        break

