"""
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 2, 100)  # Sample data.

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.
"""

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
uMGF1 = mpatches.Patch(color='red', label='BdUMGF1')
uMGF2 = mpatches.Patch(color='green', label='BdUMGF2')
uMGF3 = mpatches.Patch(color='blue', label='BdUMGF3')
ortho1 = mpatches.Patch(color='cyan', label='BdOMGF1')
ortho2 = mpatches.Patch(color='magenta', label='BdOMGF2')
ortho3 = mpatches.Patch(color='orange', label='BdOMGF3')
gpi = mpatches.Patch(color=(0.78, 0.59, 0.39), label='GPI') #brown
ap = mpatches.Patch(color=(0.53, 0.81, 0.98), label='AP') #light sky blue
centromere = mpatches.Patch(color=(0.39, 0.39, 0.39), label='Centromere') #grey
ax.legend(handles=[uMGF1, uMGF2, uMGF3, ortho1, ortho2, ortho3, gpi, ap, centromere])

plt.savefig("legends.png")