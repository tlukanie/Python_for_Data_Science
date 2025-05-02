import matplotlib.pyplot as plt
import numpy as np

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a line plot
plt.plot(x, y, color="blue")

# Add title and labels
plt.title("Example Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Add legend
#plt.legend()

# Show the plot
plt.show()