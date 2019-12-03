# Import the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Initialize the data
x = 10 ** np.arange(1, 10)
y = x * 2
data = pd.DataFrame(data={'x': x, 'y': y})

# Create an lmplot
grid = sns.lmplot('x', 'y', data, size=7, truncate=True, scatter_kws={"s": 100})

# Rotate the labels on x-axis
grid.set_xticklabels(rotation=30)

# Show the plot
plt.show()