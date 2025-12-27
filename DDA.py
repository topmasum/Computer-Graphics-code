from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Line endpoints
x1, y1 = 2, 2
x2, y2 = 8, 6
points = []

# DDA Line Algorithm
def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x1, y1
    for _ in range(int(steps) + 1):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc

dda_line(x1, y1, x2, y2)

# Draw grid
def draw_grid():
    glColor3f(0.8, 0.8, 0.8)  # light gray
    glLineWidth(1)
    glBegin(GL_LINES)
    # Vertical lines
    for i in range(11):
        glVertex2f(i, 0)
        glVertex2f(i, 10)
    # Horizontal lines
    for i in range(11):
        glVertex2f(0, i)
        glVertex2f(10, i)
    glEnd()

# OpenGL display
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    draw_grid()
    
    # Draw DDA line
    glColor3f(0, 0, 0)  # black pixels
    glPointSize(5)
    glBegin(GL_POINTS)
    for x, y in points:
        glVertex2f(x, y)
    glEnd()
    
    glFlush()

# Initialize OpenGL
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"DDA Line with Grid  OpenGL")
glClearColor(1, 1, 1, 1)
gluOrtho2D(0, 10, 0, 10)  # match matplotlib limits
glutDisplayFunc(display)
glutMainLoop()
