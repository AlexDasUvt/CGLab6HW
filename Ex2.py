import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

A7 = [-1.4, 3.4] # Point A7
A8 = [2.4, -9.2] # Point A8

points = np.array([[5, -1], [7, -1], [9, -1], [7, -3], [11, -1], [-9,3], A7, A8])

vor = Voronoi(points)
fig, ax = plt.subplots(figsize=(6, 6))

voronoi_plot_2d(vor, ax=ax)
ax.scatter(points[:, 0], points[:, 1], color='red')
ax.set_title("Voronoi Diagram")
ax.set_xlim(-10, 15)
ax.set_ylim(-10, 15)

plt.tight_layout()
plt.show()