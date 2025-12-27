import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8,6))
ax.set_xlim(0, 20)
ax.set_ylim(0, 15)
ax.axis('off')

# -------- Steps --------
for i in range(4):
    ax.add_patch(
        plt.Rectangle((2 - i*0.5, 1 + i*0.5),
                      16 + i, 0.5,
                      color='#8B0000')
    )

# -------- Red Sun (Centered) --------
ax.add_patch(plt.Circle((10, 7), 2, color='red'))

# -------- Pillar Function --------
def pillar(x, width, height):
    ax.add_patch(
        plt.Rectangle((x, 3), width, height,
                       fill=False, linewidth=3,
                       edgecolor='black')
    )
    # Add middle line
    ax.plot([x + width/2, x + width/2], [3, 3 + height], color='black', linewidth=1.5)

# -------- Side Pillars --------
pillar(3, 1.2, 6)
pillar(5.5, 1.2, 8)
pillar(13.3, 1.2, 8)
pillar(15.8, 1.2, 6)

# -------- Middle Pillar --------
pillar(9.2, 1.6, 8)

# -------- Slanted Upper Frames (KEY PART) --------
left_slant = plt.Polygon(
    [
        [9.2, 11],    # bottom-left stays the same
        [10.8, 11],   # bottom-right shifted to match pillar width
        [11.3, 14],   # top-right shifted by same amount (1.0)
        [9.7, 14]     # top-left shifted by same amount (1.0)
    ],
    fill=False, linewidth=3, edgecolor='black'
)

ax.add_patch(left_slant)

plt.title("Shahid Minar – Slanted Upper Middle Structure with Center Lines")
plt.show()
