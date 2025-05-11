from random import choice

class RandomWalk:
    '''A class to generate random walks'''
    
    def __init__(self, num_points = 5000):
        '''Initialize the walks'''

        self.num_points = num_points
        
        #All walks starts at zero as (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    
    def fill_walks(self):
        '''Fill the walks by steps of each co-ordinates using choice'''

        while len(self.x_values) < self.num_points:

            x_choice = choice([1, -1])
            x_distance = choice ([0, 1, 2, 3, 4, 5])
            x_step = x_choice * x_distance

            y_choice = choice([1, -1])
            y_distance = choice ([0, 1, 2, 3, 4, 5])
            y_step = y_choice * y_distance

            #Ignore if no movement
            if x_step==0 and y_step==0:
                continue
            
            #Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

