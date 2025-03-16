import numpy as np
import matplotlib.pyplot as plt

# Define fixed pivot coordinates
A = np.array([0, 0])    # Fixed pivot 1
D = np.array([4, 0])    # Fixed pivot 2
G = np.array([2, 3])    # Fixed pivot 3

# Define link lengths (cranks + couplers + rockers)
L_AB = 1.0   # Crank 1
L_BC = 2.0   # Coupler 1
L_CD = 2.5   # Rocker 1
L_DE = 1.0   # Crank 2
L_EF = 2.0   # Coupler 2
L_FG = 2.0   # Rocker 2
L_GH = 1.0   # Crank 3
L_HI = 2.0   # Coupler 3
L_IA = 1.5   # Rocker 3

# Define crank angles (static visualization)
theta1 = np.pi/4    # Angle for crank AB
theta2 = -np.pi/6   # Angle for crank DE
theta3 = np.pi/3    # Angle for crank GH

# Compute joint positions
# First four-bar chain (A-B-C-D)
B = A + L_AB * np.array([np.cos(theta1), np.sin(theta1)])
C = B + L_BC * np.array([np.cos(theta1 + np.pi/3), np.sin(theta1 + np.pi/3)])

# Second four-bar chain (D-E-F-G)
E = D + L_DE * np.array([np.cos(theta2), np.sin(theta2)])
F = E + L_EF * np.array([np.cos(theta2 - np.pi/4), np.sin(theta2 - np.pi/4)])

# Third four-bar chain (G-H-I-A)
H = G + L_GH * np.array([np.cos(theta3), np.sin(theta3)])
I = H + L_HI * np.array([np.cos(theta3 + np.pi/5), np.sin(theta3 + np.pi/5)])

# Initialize plot
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(-2, 6)
ax.set_ylim(-2, 6)
ax.set_aspect('equal')
ax.grid(True)
plt.title("Six-Bar Mechanism with Three Cranks (Static Diagram)")

# Plot fixed pivots
ax.plot(A[0], A[1], 'ks', markersize=10, label='Fixed Pivots')
ax.plot(D[0], D[1], 'ks', markersize=10)
ax.plot(G[0], G[1], 'ks', markersize=10)

# Plot all links with distinct colors
# First chain (A-B-C-D)
ax.plot([A[0], B[0]], [A[1], B[1]], 'b-o', lw=2, label='Crank 1 (AB)')
ax.plot([B[0], C[0]], [B[1], C[1]], 'g-o', lw=2, label='Coupler 1 (BC)')
ax.plot([C[0], D[0]], [C[1], D[1]], 'r-o', lw=2, label='Rocker 1 (CD)')

# Second chain (D-E-F-G)
ax.plot([D[0], E[0]], [D[1], E[1]], 'c-o', lw=2, label='Crank 2 (DE)')
ax.plot([E[0], F[0]], [E[1], F[1]], 'm-o', lw=2, label='Coupler 2 (EF)')
ax.plot([F[0], G[0]], [F[1], G[1]], 'y-o', lw=2, label='Rocker 2 (FG)')

# Third chain (G-H-I-A)
ax.plot([G[0], H[0]], [G[1], H[1]], 'orange', marker='o', lw=2, label='Crank 3 (GH)')
ax.plot([H[0], I[0]], [H[1], I[1]], 'purple', marker='o', lw=2, label='Coupler 3 (HI)')
ax.plot([I[0], A[0]], [I[1], A[1]], 'brown', marker='o', lw=2, label='Rocker 3 (IA)')

# Add labels and legend
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()