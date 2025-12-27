import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create figure
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis('off')

# Car body (red)
body = plt.Rectangle((0, 1.5), 3, 1, color='red')
ax.add_patch(body)

# Car top (blue)
top = plt.Rectangle((0.7, 2.3), 1.6, 0.7, color='blue')
ax.add_patch(top)

# Wheels (black)
wheel1 = plt.Circle((0.7, 1.5), 0.3, color='black')
wheel2 = plt.Circle((2.3, 1.5), 0.3, color='black')
ax.add_patch(wheel1)
ax.add_patch(wheel2)

# Animation function
def move(frame):
    x = frame * 0.05
    body.set_x(x)
    top.set_x(x + 0.7)
    wheel1.center = (x + 0.7, 1.5)
    wheel2.center = (x + 2.3, 1.5)
    return body, top, wheel1, wheel2

# Animate
ani = FuncAnimation(fig, move, frames=120, interval=50)

plt.show()
