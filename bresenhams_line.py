import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    p = 2*dy - dx
    x, y = x1, y1

    plt.plot(x, y, 'ro')

    while x < x2:
        if p < 0:
            p = p + 2*dy
        else:
            p = p + 2*(dy - dx)
            y += 1

        x += 1
        plt.plot(x, y, 'ro')

# Draw line
bresenham_line(2, 2, 8, 5)

plt.title("Bresenham Line Drawing Algorithm")
plt.grid(True)
plt.gca().set_aspect('equal')
plt.show()
