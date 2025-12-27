from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Circle properties
xc, yc = 10, 10  # center
r = 6             # radius
points = []       # list to store circle points

# Midpoint Circle Algorithm
def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    while x <= y:
        # 8 symmetric points
        points.extend([
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x)
        ])

        if p < 0:
            p = p + 2*x + 3
        else:
            p = p + 2*(x - y) + 5
            y -= 1
        x += 1

# Generate circle points
midpoint_circle(xc, yc, r)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)  # red points
    glPointSize(3)    # make points visible
    glBegin(GL_POINTS)
    for x, y in points:
        glVertex2f(x, y)
    glEnd()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Midpoint Circle Algorithm  OpenGL")

    glClearColor(1,1,1,1)  # white background
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 25, 0, 25)  # match your matplotlib limits

    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
