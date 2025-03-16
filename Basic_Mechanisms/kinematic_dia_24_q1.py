import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define geometric parameters
BASE_RADIUS = 3.0     # Radius of the base triangle
PLATFORM_RADIUS = 1.0 # Radius of the moving platform
L1 = 2.0              # Length of first link in each limb
L2 = 1.5              # Length of second link in each limb

# Initialize figure
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.grid(True)

# Base triangle (fixed)
base_angles = np.array([0, 2*np.pi/3, 4*np.pi/3])
base_points = BASE_RADIUS * np.column_stack([np.cos(base_angles), np.sin(base_angles)])

# Moving platform (initial position)
platform_angles = base_angles.copy()
platform_points = PLATFORM_RADIUS * np.column_stack([np.cos(platform_angles), np.sin(platform_angles)])

# Initialize links and platform
limb_lines = [ax.plot([], [], 'b-o', lw=2)[0] for _ in range(3)]
platform_line, = ax.plot([], [], 'r-o', lw=2)
base_line, = ax.plot(np.append(base_points[:,0], base_points[0,0]),
                    np.append(base_points[:,1], base_points[0,1]), 'k-o', lw=2)

def update_kinematics(theta1, theta2, theta3):
    """Compute joint positions for given actuator angles"""
    B = np.zeros((3, 2))
    C = np.zeros((3, 2))
    
    # For each limb (simplified kinematics)
    for i, theta in enumerate([theta1, theta2, theta3]):
        # First revolute joint (actuated)
        B[i] = base_points[i] + L1 * np.array([np.cos(theta), np.sin(theta)])
        
        # Second revolute joint (passive, simplified)
        C[i] = B[i] + L2 * np.array([np.cos(theta + np.pi/3), np.sin(theta + np.pi/3)])
    
    return B, C

def animate(frame):
    # Update actuator angles (simple rotation)
    theta = frame * np.pi / 30
    theta1, theta2, theta3 = theta, theta + np.pi/3, theta - np.pi/3
    
    # Compute joint positions
    B, C = update_kinematics(theta1, theta2, theta3)
    
    # Update limb lines
    for i in range(3):
        limb_lines[i].set_data([base_points[i,0], B[i,0], C[i,0]],
                              [base_points[i,1], B[i,1], C[i,1]])
    
    # Update platform (connect all C points)
    platform_line.set_data(np.append(C[:,0], C[0,0]), np.append(C[:,1], C[0,1]))
    
    return limb_lines + [platform_line, base_line]

# Create animation
ani = FuncAnimation(fig, animate, frames=60, interval=50, blit=True)

plt.title("3-DOF Planar Parallel Manipulator (RRR)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()