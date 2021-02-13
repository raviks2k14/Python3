from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6.
die1 = Die(8)
die2 = Die(8)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(100_000):
    result = die1.roll() + die2.roll()
    results.append(result)

# Analyze the results
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 100_000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
