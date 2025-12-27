import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create window
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# Wheel properties
radius = 1
num_spokes = 8

# Draw wheel (circle)
theta = np.linspace(0, 2*np.pi, 300)
circle, = ax.plot(radius*np.cos(theta), radius*np.sin(theta), linewidth=2)

# Draw spokes
angles = np.linspace(0, 2*np.pi, num_spokes, endpoint=False)
spokes = []
for angle in angles:
    line, = ax.plot([0, radius*np.cos(angle)],
                     [0, radius*np.sin(angle)], linewidth=2)
    spokes.append(line)

# Rotation function
def rotate(frame):
    rotation = frame * 0.1
    for i, line in enumerate(spokes):
        a = angles[i] + rotation
        line.set_data([0, radius*np.cos(a)],
                      [0, radius*np.sin(a)])
    return spokes

# Animate
ani = FuncAnimation(fig, rotate, frames=200, interval=50)

plt.show()
