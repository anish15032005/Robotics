import numpy as np
import matplotlib.pyplot as plt

# Function to create transformation matrix
def transformation_matrix(theta, length):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0, length * np.cos(theta)],
        [np.sin(theta),  np.cos(theta), 0, length * np.sin(theta)],
        [0,              0,             1, 0],
        [0,              0,             0, 1]
    ])

# Parameters
L1 = 1  # Length of Link 1
L2 = 1  # Length of Link 2
theta1 = np.pi / 4  # Joint angle for Link 1 (in radians)
theta2 = np.pi / 3  # Joint angle for Link 2 (in radians)

# Transformation Matrices
T1 = transformation_matrix(theta1, L1)
T2 = transformation_matrix(theta2, L2)

# Combined Transformation Matrix
T = np.dot(T1, T2)

# Joint positions
joint1 = np.array([0, 0])
joint2 = T1[:2, 3]
end_effector = T[:2, 3]

# Visualization
plt.figure()
plt.grid()
plt.axis('equal')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('2-Link Planar Robotic Arm Manipulator')

# Plot Links
plt.plot([joint1[0], joint2[0]], [joint1[1], joint2[1]], 'r-', linewidth=2, label='Link 1')  # Link 1
plt.plot([joint2[0], end_effector[0]], [joint2[1], end_effector[1]], 'b-', linewidth=2, label='Link 2')  # Link 2

# Plot Joints
plt.scatter(joint1[0], joint1[1], color='k', s=50, label='Base')  # Base
plt.scatter(joint2[0], joint2[1], color='k', s=50, label='Joint 1')  # Joint 1
plt.scatter(end_effector[0], end_effector[1], color='g', s=50, label='End Effector')  # End Effector

plt.legend()
plt.show()


import time as t 
for t in np.linspace(0, np.pi, 100):
    theta1 = t
    theta2 = t / 2
    T1 = transformation_matrix(theta1, L1)
    T2 = transformation_matrix(theta2, L2)
    T = np.dot(T1, T2)
    joint2 = T1[:2, 3]
    end_effector = T[:2, 3]
    
    plt.clf()
    plt.grid()
    plt.axis('equal')
    plt.plot([joint1[0], joint2[0]], [joint1[1], joint2[1]], 'r-', linewidth=2)
    plt.plot([joint2[0], end_effector[0]], [joint2[1], end_effector[1]], 'b-', linewidth=2)
    plt.scatter(joint1[0], joint1[1], color='k', s=50)
    plt.scatter(joint2[0], joint2[1], color='k', s=50)
    plt.scatter(end_effector[0], end_effector[1], color='g', s=50)
    plt.pause(0.1)
