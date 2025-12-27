import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))
    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1

    for i in range(steps + 1):
        # draw pixel as a filled square
        plt.gca().add_patch(
            plt.Rectangle((round(x), round(y)), 1, 1, color='black')
        )
        x += x_inc
        y += y_inc

# Draw line
dda_line(2, 2, 8, 6)

plt.xlim(0, 10)
plt.ylim(0, 10)
plt.gca().set_aspect('equal')
plt.grid(True)
plt.title("DDA Line Drawing with Pixel Coverage")
plt.show()
