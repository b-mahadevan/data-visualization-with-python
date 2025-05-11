from die import Die

import plotly.express as px

die = Die()

#Store the result as List after the single die rolled
results = []

#Rolling the single die 1000 times
for roll in range(2000):
    output = die.roll()
    results.append(output)

#Store the count of result of single side as List
frequencies = []

die_side = range(1, die.num_sides+1)

for roll in die_side:

    output = results.count(roll)
    frequencies.append(output)

title = 'Results and their Frequencies of Single Die Rolled 2000 Times'
label = {'x': 'Results', 'y': 'Frequencies of Results'}

#Plot the bar chart
fig = px.bar(x=die_side, y=frequencies, title=title, labels=label)
fig.show()