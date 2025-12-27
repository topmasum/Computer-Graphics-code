from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin, pi

# Car position
car_x = -1.2
speed = 0.01

def draw_rectangle(x, y, w, h, r, g, b):
    glColor3f(r, g, b)
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x+w, y)
    glVertex2f(x+w, y+h)
    glVertex2f(x, y+h)
    glEnd()

def draw_circle(cx, cy, r):
    glBegin(GL_TRIANGLE_FAN)
    for i in range(50):
        angle = 2 * pi * i / 50
        glVertex2f(cx + r*cos(angle), cy + r*sin(angle))
    glEnd()

def display():
    global car_x
    glClear(GL_COLOR_BUFFER_BIT)

    # Move car
    glPushMatrix()
    glTranslatef(car_x, 0, 0)

    # Car body
    draw_rectangle(-0.4, -0.1, 0.8, 0.2, 1, 0, 0)

    # Car top
    draw_rectangle(-0.2, 0.1, 0.4, 0.2, 0, 0, 1)

    # Wheels
    glColor3f(0, 0, 0)
    draw_circle(-0.25, -0.1, 0.08)
    draw_circle( 0.25, -0.1, 0.08)

    glPopMatrix()
    glutSwapBuffers()

def update(value):
    global car_x
    car_x += speed

    if car_x > 1.2:
        car_x = -1.2

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

# OpenGL setup
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 400)
glutCreateWindow(b"Simple Moving Car - OpenGL")

glClearColor(1, 1, 1, 1)
gluOrtho2D(-1, 1, -1, 1)

glutDisplayFunc(display)
glutTimerFunc(0, update, 0)
glutMainLoop()
