from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import sin, cos, pi

# Window size
width, height = 600, 600

# Wheel properties
radius = 1.0
num_spokes = 8
theta_steps = 100  # for circle approximation
rotation_angle = 0.0  # global rotation

def draw_circle(cx, cy, r, steps=100):
    glBegin(GL_LINE_LOOP)
    for i in range(steps):
        angle = 2 * pi * i / steps
        glVertex2f(cx + r * cos(angle), cy + r * sin(angle))
    glEnd()

def draw_wheel():
    global rotation_angle
    # Draw circle
    glColor3f(0, 0, 0)
    draw_circle(0, 0, radius, theta_steps)
    
    # Draw spokes
    for i in range(num_spokes):
        angle = 2 * pi * i / num_spokes + rotation_angle
        glBegin(GL_LINES)
        glVertex2f(0, 0)
        glVertex2f(radius * cos(angle), radius * sin(angle))
        glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    draw_wheel()
    
    glutSwapBuffers()

def timer(value):
    global rotation_angle
    rotation_angle += 0.1  # rotation speed
    if rotation_angle > 2*pi:
        rotation_angle -= 2*pi
    glutPostRedisplay()
    glutTimerFunc(50, timer, 0)  # call every 50ms

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Rotating Wheel  OpenGL")
    
    glClearColor(1,1,1,1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-2, 2, -2, 2)
    
    glutDisplayFunc(display)
    glutTimerFunc(0, timer, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
