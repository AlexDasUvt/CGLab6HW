import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

points = np.array(
    [
        [1, -1],
        [0, 0],
        [-1, 1],
        [-2, 2],
        [-3, 3],
        [-4, 4],
        [0, 0],
        [1, -1],
        [2, -2],
        [3, -3],
        [4, -4],
        [5, -5],
        [0, 1],
        [0, 2],
        [0, 3],
        [0, 4],
        [0, 5],
    ]
)

vor = Voronoi(points)
fig, ax = plt.subplots(figsize=(6, 6))

voronoi_plot_2d(vor, ax=ax)
ax.scatter(points[:, 0], points[:, 1], color="red")
ax.set_title("Voronoi Diagram")
ax.set_xlim(-10, 15)
ax.set_ylim(-10, 15)

plt.tight_layout()
plt.show()
