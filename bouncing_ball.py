from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin, pi

# Ball properties
x, y = 0.0, 0.0
dx, dy = 0.02, 0.03
radius = 0.1

def draw_circle(cx, cy, r):
    glBegin(GL_TRIANGLE_FAN)
    for i in range(50):
        angle = 2 * pi * i / 50
        glVertex2f(cx + r * cos(angle), cy + r * sin(angle))
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)  # red ball
    draw_circle(x, y, radius)
    glutSwapBuffers()

def update(value):
    global x, y, dx, dy

    x += dx
    y += dy

    # Bounce from walls
    if x + radius > 1 or x - radius < -1:
        dx = -dx
    if y + radius > 1 or y - radius < -1:
        dy = -dy

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)  # ~60 FPS

# OpenGL setup
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Bouncing Ball - OpenGL")

glClearColor(1, 1, 1, 1)
gluOrtho2D(-1, 1, -1, 1)

glutDisplayFunc(display)
glutTimerFunc(0, update, 0)
glutMainLoop()
