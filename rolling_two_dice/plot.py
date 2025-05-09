from die import Die

die1 = Die()
die2 = Die()

#Store the result as List after the single die rolled
results = []

#Rolling the single die 1000 times
for roll in range(2000):
    output = die1.roll() + die2.roll()
    results.append(output)

#Store the count of result of single side as List
frequencies = []

max_results = die1.num_sides + die2.num_sides
die_side = range(2, max_results+1)

for roll in die_side:

    output = results.count(roll)
    frequencies.append(output)

title = 'Results and their Frequencies of Two Dice Rolled 2000 Times'
label = {'x': 'Results', 'y': 'Frequencies of Results'}

#Plot the bar chart
fig = px.bar(x=die_side, y=frequencies, title=title, labels=label)
fig.show()
