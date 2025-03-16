import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define vertices of a tesseract
vertices = np.array([[0, 0, 0, 0],
                     [0, 0, 0, 1],
                     [0, 0, 1, 0],
                     [0, 0, 1, 1],
                     [0, 1, 0, 0],
                     [0, 1, 0, 1],
                     [0, 1, 1, 0],
                     [0, 1, 1, 1],
                     [1, 0, 0, 0],
                     [1, 0, 0, 1],
                     [1, 0, 1, 0],
                     [1, 0, 1, 1],
                     [1, 1, 0, 0],
                     [1, 1, 0, 1],
                     [1, 1, 1, 0],
                     [1, 1, 1, 1]])

# Projection to 3D
projection_matrix = np.array([[1, 0, 0, 0],
                               [0, 1, 0, 0],
                               [0, 0, 1, 0]])
vertices_3d = vertices @ projection_matrix.T

# Define edges of a tesseract
edges = [
    (0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3), (2, 6), 
    (3, 7), (4, 5), (4, 6), (5, 7), (6, 7),
    (8, 9), (8, 10), (8, 12), (9, 11), (9, 13), (10, 11), 
    (10, 14), (11, 15), (12, 13), (12, 14), (13, 15), (14, 15),
    (0, 8), (1, 9), (2, 10), (3, 11), (4, 12), (5, 13), 
    (6, 14), (7, 15)
]

# Plotting the tesseract
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
for edge in edges:
    x_coords = [vertices_3d[edge[0], 0], vertices_3d[edge[1], 0]]
    y_coords = [vertices_3d[edge[0], 1], vertices_3d[edge[1], 1]]
    z_coords = [vertices_3d[edge[0], 2], vertices_3d[edge[1], 2]]
    ax.plot(x_coords, y_coords, z_coords, 'b')

# Set plot limits and labels
ax.set_xlim([-0.5, 1.5])
ax.set_ylim([-0.5, 1.5])
ax.set_zlim([-0.5, 1.5])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("3D Projection of a Tesseract")
plt.show()