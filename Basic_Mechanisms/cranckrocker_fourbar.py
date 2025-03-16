import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def get_intersections(Bx, By, Dx, Dy, coupler_length, rocker_length):
    """Find intersection points of two circles (B and D)"""
    d = np.hypot(Dx - Bx, Dy - By)
    if d > coupler_length + rocker_length or d < abs(coupler_length - rocker_length):
        return None  # No intersection
    a = (coupler_length**2 - rocker_length**2 + d**2) / (2 * d)
    h = np.sqrt(coupler_length**2 - a**2)
    xm = Bx + a * (Dx - Bx) / d
    ym = By + a * (Dy - By) / d
    return (
        (xm + h * (Dy - By) / d, ym - h * (Dx - Bx) / d),
        (xm - h * (Dy - By) / d, ym + h * (Dx - Bx) / d)
    )

# Link lengths (mm)
ground_length = 45
crank_length = 20
coupler_length = 56
rocker_length = 73

# Crank angle = 120°
theta2 = np.radians(120)
Bx = crank_length * np.cos(theta2)
By = crank_length * np.sin(theta2)
Dx, Dy = ground_length, 0

# Solve for coupler-rocker joint (C)
intersections = get_intersections(Bx, By, Dx, Dy, coupler_length, rocker_length)
if intersections:
    (C1x, C1y), (C2x, C2y) = intersections
    Cx, Cy = (C1x, C1y) if C1y > C2y else (C2x, C2y)  # Select upper solution

    # Plot mechanism
    plt.figure(figsize=(8, 8))
    plt.plot([0, Bx], [0, By], 'b-o', lw=2, label='Crank (AB)')
    plt.plot([Bx, Cx], [By, Cy], 'g-o', lw=2, label='Coupler (BC)')
    plt.plot([Cx, Dx], [Cy, Dy], 'r-o', lw=2, label='Rocker (CD)')
    plt.plot([0, Dx], [0, Dy], 'k-s', lw=2, markersize=10, label='Ground (AD)')
    plt.xlim(-30, 80); plt.ylim(-30, 80)
    plt.gca().set_aspect('equal'); plt.grid(True)
    plt.title(f'Crank-Rocker at θ₂ = 120°'); plt.legend()
    plt.show()

# Calculate limiting positions
AC_extended = crank_length + coupler_length
cos_angle_ext = (ground_length**2 + AC_extended**2 - rocker_length**2) / (2 * ground_length * AC_extended)
angle_ext = np.degrees(np.arccos(cos_angle_ext))

AC_folded = coupler_length - crank_length
cos_angle_fold = (ground_length**2 + AC_folded**2 - rocker_length**2) / (2 * ground_length * AC_folded)
angle_fold = np.degrees(np.arccos(cos_angle_fold))

# Rocker angles
C_ext = AC_extended * np.cos(np.radians(angle_ext)), AC_extended * np.sin(np.radians(angle_ext))
C_fold = AC_folded * np.cos(np.radians(angle_fold)), AC_folded * np.sin(np.radians(angle_fold))
θ_rocker_max = np.degrees(np.arctan2(C_fold[1], C_fold[0] - ground_length))
θ_rocker_min = np.degrees(np.arctan2(C_ext[1], C_ext[0] - ground_length))

# Time ratio
Δ_theta = abs(angle_fold - angle_ext)
time_ratio = Δ_theta / (360 - Δ_theta)

print(f"Limiting positions of the rocker:")
print(f"  Maximum angle: {θ_rocker_max:.2f}°")
print(f"  Minimum angle: {θ_rocker_min:.2f}°\n")
print(f"Time ratio (Q): {time_ratio:.3f} (Forward Stroke/Return Stroke)")

def animate_mechanism(crank_length, coupler_length, rocker_length, ground_length, frames=360):
    fig, ax = plt.subplots()
    ax.set_xlim(-30, 80)
    ax.set_ylim(-30, 80)
    ax.set_aspect('equal')
    ax.grid(True)
    
    crank_line, = ax.plot([], [], 'b-o', lw=2, label='Crank (AB)')
    coupler_line, = ax.plot([], [], 'g-o', lw=2, label='Coupler (BC)')
    rocker_line, = ax.plot([], [], 'r-o', lw=2, label='Rocker (CD)')
    ground_line, = ax.plot([0, ground_length], [0, 0], 'k-s', lw=2, markersize=10, label='Ground (AD)')
    ax.legend()

    def init():
        crank_line.set_data([], [])
        coupler_line.set_data([], [])
        rocker_line.set_data([], [])
        return crank_line, coupler_line, rocker_line

    def update(frame):
        theta2 = np.radians(frame)
        Bx = crank_length * np.cos(theta2)
        By = crank_length * np.sin(theta2)
        Dx, Dy = ground_length, 0

        intersections = get_intersections(Bx, By, Dx, Dy, coupler_length, rocker_length)
        if intersections:
            (C1x, C1y), (C2x, C2y) = intersections
            Cx, Cy = (C1x, C1y) if C1y > C2y else (C2x, C2y)

            crank_line.set_data([0, Bx], [0, By])
            coupler_line.set_data([Bx, Cx], [By, Cy])
            rocker_line.set_data([Cx, Dx], [Cy, Dy])
        return crank_line, coupler_line, rocker_line

    ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True)
    plt.show()

# Animate the mechanism
animate_mechanism(crank_length, coupler_length, rocker_length, ground_length)