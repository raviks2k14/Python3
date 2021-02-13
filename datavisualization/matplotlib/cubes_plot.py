import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')

fig, ax = plt.subplots()

# ax.plot(x_values, y_values, linewidth=3)


# Set chart title and label axes
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# ax.scatter(x_values, y_values)

plt.show()
