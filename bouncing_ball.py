import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create window
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis('off')

# Ball
ball = plt.Circle((1, 1), 0.3, color='red')
ax.add_patch(ball)

# Speed
dx, dy = 0.05, 0.05
x, y = 1, 1

# Animation function
def bounce(frame):
    global x, y, dx, dy

    x += dx
    y += dy

    # Bounce from walls
    if x <= 0.3 or x >= 9.7:
        dx = -dx
    if y <= 0.3 or y >= 4.7:
        dy = -dy

    ball.center = (x, y)
    return ball,

# Animate
ani = FuncAnimation(fig, bounce, frames=300, interval=20)

plt.show()
