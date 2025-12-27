from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Line endpoints
x1, y1 = 2, 2
x2, y2 = 8, 5
points = []

# Bresenham Line Algorithm
def bresenham_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    p = 2 * dy - dx
    x, y = x1, y1
    points.append((x, y))

    while x < x2:
        if p < 0:
            p = p + 2 * dy
        else:
            p = p + 2 * (dy - dx)
            y += 1
        x += 1
        points.append((x, y))

# Generate line points
bresenham_line(x1, y1, x2, y2)

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw grid
    glColor3f(0.8, 0.8, 0.8)
    glBegin(GL_LINES)
    for i in range(11):
        glVertex2f(i, 0)
        glVertex2f(i, 10)
        glVertex2f(0, i)
        glVertex2f(10, i)
    glEnd()

    # Draw Bresenham points
    glColor3f(1, 0, 0)  # red points
    glPointSize(6)
    glBegin(GL_POINTS)
    for x, y in points:
        glVertex2f(x, y)
    glEnd()

    glFlush()

# OpenGL setup
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Bresenham Line Algorithm  OpenGL")

glClearColor(1, 1, 1, 1)
gluOrtho2D(0, 10, 0, 10)

glutDisplayFunc(display)
glutMainLoop()
