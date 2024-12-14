import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, Delaunay, voronoi_plot_2d, delaunay_plot_2d

points = np.array([[3, -5], [-6, 6], [6, -4], [5, -5], [9, 10]])

vor = Voronoi(points)
del_tri = Delaunay(points)
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

voronoi_plot_2d(vor, ax=ax[0])
ax[0].scatter(points[:, 0], points[:, 1], color='red')
ax[0].set_title("Voronoi Diagram")
ax[0].set_xlim(-10, 15)
ax[0].set_ylim(-10, 15)

delaunay_plot_2d(del_tri, ax=ax[1])
ax[1].scatter(points[:, 0], points[:, 1], color='blue')
ax[1].set_title("Delaunay Triangulation")
ax[1].set_xlim(-10, 15)
ax[1].set_ylim(-10, 15)

plt.tight_layout()
plt.show()