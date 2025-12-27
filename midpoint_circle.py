import matplotlib.pyplot as plt

def plot_point(x, y):
    plt.plot(x, y, 'ro')   # red dot

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    while x <= y:
        plot_point(xc + x, yc + y)
        plot_point(xc - x, yc + y)
        plot_point(xc + x, yc - y)
        plot_point(xc - x, yc - y)
        plot_point(xc + y, yc + x)
        plot_point(xc - y, yc + x)
        plot_point(xc + y, yc - x)
        plot_point(xc - y, yc - x)

        if p < 0:
            p = p + 2*x + 3
        else:
            p = p + 2*(x - y) + 5
            y -= 1

        x += 1

# Draw circle
midpoint_circle(10, 10, 6)

plt.xlim(0, 25)
plt.ylim(0, 25)
plt.gca().set_aspect('equal')
plt.grid(True)
plt.title("Midpoint Circle Algorithm (Red Points)")
plt.show()
