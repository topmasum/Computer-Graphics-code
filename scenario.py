import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8,6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# -------- Sky --------
sky = plt.Rectangle((0, 4), 10, 6, color='skyblue')
ax.add_patch(sky)

# -------- Grass Ground --------
ground = plt.Rectangle((0, 0), 10, 4, color='lightgreen')
ax.add_patch(ground)

# -------- Sun --------
sun = plt.Circle((8, 8), 0.8, color='yellow')
ax.add_patch(sun)

# -------- Cloud --------
cloud_color = 'white'
ax.add_patch(plt.Circle((2, 8), 0.5, color=cloud_color))
ax.add_patch(plt.Circle((2.6, 8.2), 0.6, color=cloud_color))
ax.add_patch(plt.Circle((3.2, 8), 0.5, color=cloud_color))

# -------- House --------
house = plt.Rectangle((4, 2), 3, 2, color='burlywood')
roof = plt.Polygon([[4,4],[5.5,5.6],[7,4]], color='maroon')
door = plt.Rectangle((5.2, 2), 0.6, 1.2, color='saddlebrown')
window1 = plt.Rectangle((4.3, 2.8), 0.5, 0.5, color='lightblue')
window2 = plt.Rectangle((6.2, 2.8), 0.5, 0.5, color='lightblue')

ax.add_patch(house)
ax.add_patch(roof)
ax.add_patch(door)
ax.add_patch(window1)
ax.add_patch(window2)

# -------- Tree --------
trunk = plt.Rectangle((1.3, 2), 0.4, 1.5, color='sienna')
leaves = plt.Circle((1.5, 4), 1.0, color='forestgreen')
ax.add_patch(trunk)
ax.add_patch(leaves)

# -------- Grass Blades --------
for x in range(0, 20):
    ax.plot([x*0.4, x*0.5+0.1], [1.8, 2.2], color='green')

plt.show()
