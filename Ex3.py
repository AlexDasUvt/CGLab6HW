import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

points = {
    'A': (-1, 6),
    'B': (-1, -1),
    'C': (4, 7),
    'D': (6, 7),
    'E': (1, -1),
    'F': (-5, 3),
    'P': (-2, 3)
}

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def compute_mst(lambda_value):
    points['Q'] = (2 - lambda_value, 3)
    
    G = nx.Graph()
    for p1 in points:
        for p2 in points:
            if p1 != p2:
                dist = euclidean_distance(points[p1], points[p2])
                G.add_edge(p1, p2, weight=dist)

    mst = nx.minimum_spanning_tree(G)
    
    return mst

lambda_values = np.linspace(-10, 10, 1000)
mst_lengths = [compute_mst(lam).size(weight='weight') for lam in lambda_values]

min_mst_length = min(mst_lengths)
optimal_lambda = lambda_values[mst_lengths.index(min_mst_length)]

print(f"The optimal lambda value is: {optimal_lambda}")
print(f"The minimum MST length is: {min_mst_length}")

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(lambda_values, mst_lengths)
plt.xlabel('Lambda')
plt.ylabel('MST Length')
plt.title('MST Length vs Lambda')

lambda_value = 5
mst = compute_mst(lambda_value)
plt.subplot(1, 2, 2)
pos = {point: points[point] for point in points}

nx.draw(mst, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=10)
labels = nx.get_edge_attributes(mst, 'weight')
nx.draw_networkx_edge_labels(mst, pos, edge_labels={k: f"{v:.2f}" for k, v in labels.items()})

plt.title(f'Minimum Spanning Tree (lambda = {lambda_value})')

plt.tight_layout()
plt.show()