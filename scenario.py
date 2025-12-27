from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import sin, cos

# Window size
width, height = 800, 600

def draw_rect(x, y, w, h, color=(0,0,0)):
    glColor3f(*color)
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + w, y)
    glVertex2f(x + w, y + h)
    glVertex2f(x, y + h)
    glEnd()

def draw_polygon(vertices, color=(0,0,0)):
    glColor3f(*color)
    glBegin(GL_POLYGON)
    for x, y in vertices:
        glVertex2f(x, y)
    glEnd()

def draw_circle(cx, cy, r, color=(0,0,0), segments=50):
    glColor3f(*color)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx, cy)
    for i in range(segments+1):
        angle = 2 * 3.14159 * i / segments
        glVertex2f(cx + r * cos(angle), cy + r * sin(angle))
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Sky
    draw_rect(0, 4, 10, 6, color=(0.53, 0.81, 0.98))  # skyblue
    
    # Grass ground
    draw_rect(0, 0, 10, 4, color=(0.56, 0.93, 0.56))  # lightgreen

    # Sun
    draw_circle(8, 8, 0.8, color=(1,1,0))  # yellow

    # Cloud
    draw_circle(2, 8, 0.5, color=(1,1,1))
    draw_circle(2.6, 8.2, 0.6, color=(1,1,1))
    draw_circle(3.2, 8, 0.5, color=(1,1,1))

    # House
    draw_rect(4, 2, 3, 2, color=(0.87, 0.72, 0.53))  # burlywood
    draw_polygon([[4,4],[5.5,5.6],[7,4]], color=(0.5, 0, 0))  # maroon roof
    draw_rect(5.2, 2, 0.6, 1.2, color=(0.54, 0.27, 0.07))  # door
    draw_rect(4.3, 2.8, 0.5, 0.5, color=(0.68, 0.85, 0.9))  # window1
    draw_rect(6.2, 2.8, 0.5, 0.5, color=(0.68, 0.85, 0.9))  # window2

    # Tree
    draw_rect(1.3, 2, 0.4, 1.5, color=(0.62, 0.32, 0.17))  # trunk
    draw_circle(1.5, 4, 1.0, color=(0.13, 0.55, 0.13))      # leaves

    # Grass blades
    glColor3f(0, 0.5, 0)
    glLineWidth(1)
    glBegin(GL_LINES)
    for x in range(0, 20):
        glVertex2f(x*0.4, 1.8)
        glVertex2f(x*0.4+0.1, 2.2)
    glEnd()

    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"House Scene OpenGL")
    
    glClearColor(1,1,1,1)  # white background
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 10, 0, 10)
    
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
