import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

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

# Define edges of a tesseract
edges = [
    (0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3), (2, 6),
    (3, 7), (4, 5), (4, 6), (5, 7), (6, 7),
    (8, 9), (8, 10), (8, 12), (9, 11), (9, 13), (10, 11),
    (10, 14), (11, 15), (12, 13), (12, 14), (13, 15), (14, 15),
    (0, 8), (1, 9), (2, 10), (3, 11), (4, 12), (5, 13),
    (6, 14), (7, 15)
]

# Function to rotate the vertices
def rotate(vertices, angle, axis1, axis2):
    cos_theta = np.cos(angle)
    sin_theta = np.sin(angle)
    rotation_matrix = np.eye(4)
    rotation_matrix[axis1, axis1] = cos_theta
    rotation_matrix[axis1, axis2] = -sin_theta
    rotation_matrix[axis2, axis1] = sin_theta
    rotation_matrix[axis2, axis2] = cos_theta
    return vertices @ rotation_matrix.T

# Set up the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
ax.set_box_aspect([1, 1, 1])

# Animation function
def update(frame):
    ax.cla()  # Clear the plot
    rotated_vertices = rotate(vertices, frame * 0.05, 0, 3)  # Rotate in the 0-3 plane
    rotated_vertices = rotate(rotated_vertices, frame * 0.03, 1, 2)  # Rotate in the 1-2 plane
    projected_vertices = rotated_vertices[:, :3]  # Project to 3D
    for edge in edges:
        x_coords = [projected_vertices[edge[0], 0], projected_vertices[edge[1], 0]]
        y_coords = [projected_vertices[edge[0], 1], projected_vertices[edge[1], 1]]
        z_coords = [projected_vertices[edge[0], 2], projected_vertices[edge[1], 2]]
        ax.plot(x_coords, y_coords, z_coords, 'b')
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    ax.set_title("Tesseract Animation")

ani = FuncAnimation(fig, update, frames=200, interval=50)
plt.show()