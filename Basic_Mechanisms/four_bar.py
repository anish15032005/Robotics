import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define link lengths
a = 2  # Crank length
b = 4  # Coupler length
c = 5  # Rocker length
d = 4  # Fixed link length

# Define the input angle (crank angle)
theta2 = np.linspace(0, 2 * np.pi, 100)

# Function to compute positions of points B and C
def compute_positions(theta2):
    # Position of point B (end of crank)
    xB = a * np.cos(theta2)
    yB = a * np.sin(theta2)

    # Position of point C (end of rocker)
    # Using loop closure equations (simplified for visualization)
    # This assumes a valid configuration for the four-bar linkage
    xC = xB + b * np.cos(np.pi / 4)  # Simplified assumption
    yC = yB + b * np.sin(np.pi / 4)  # Simplified assumption

    return xB, yB, xC, yC

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')
ax.grid(True)

# Initialize lines for the links
link1, = ax.plot([], [], 'bo-', lw=2)  # Crank (link a)
link2, = ax.plot([], [], 'go-', lw=2)  # Coupler (link b)
link3, = ax.plot([], [], 'ro-', lw=2)  # Rocker (link c)
fixed_link, = ax.plot([0, d], [0, 0], 'k-', lw=2)  # Fixed link (link d)

# Animation function
def animate(i):
    xB, yB, xC, yC = compute_positions(theta2[i])

    # Update the positions of the links
    link1.set_data([0, xB], [0, yB])  # Crank
    link2.set_data([xB, xC], [yB, yC])  # Coupler
    link3.set_data([xC, d], [yC, 0])  # Rocker

    return link1, link2, link3

# Create the animation
ani = FuncAnimation(fig, animate, frames=len(theta2), interval=50, blit=True)

# Show the animation
plt.title('Four-Bar Linkage Motion')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.show()