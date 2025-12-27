from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
width, height = 800, 600

def draw_rect(x, y, w, h, fill=True, color=(0.0,0.0,0.0)):
    glColor3f(*color)
    if fill:
        glBegin(GL_QUADS)
    else:
        glLineWidth(3)
        glBegin(GL_LINE_LOOP)
    glVertex2f(x, y)
    glVertex2f(x + w, y)
    glVertex2f(x + w, y + h)
    glVertex2f(x, y + h)
    glEnd()

def draw_line(x1, y1, x2, y2, color=(0.0,0.0,0.0)):
    glColor3f(*color)
    glLineWidth(1.5)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def draw_polygon(vertices, fill=False, color=(0.0,0.0,0.0)):
    glColor3f(*color)
    if fill:
        glBegin(GL_POLYGON)
    else:
        glLineWidth(3)
        glBegin(GL_LINE_LOOP)
    for v in vertices:
        glVertex2f(v[0], v[1])
    glEnd()

def draw_circle(cx, cy, r, color=(1.0,0.0,0.0)):
    glColor3f(*color)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx, cy)
    for angle in range(0, 361, 5):
        rad = angle * 3.14159 / 180
        glVertex2f(cx + r * cos(rad), cy + r * sin(rad))
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Steps
    step_color = (0.545, 0, 0)  # dark red
    for i in range(4):
        draw_rect(2 - i*0.5, 1 + i*0.5, 16 + i, 0.5, fill=True, color=step_color)
    
    # Red Sun
    draw_circle(10, 7, 2, color=(1,0,0))
    
    # Side Pillars
    pillar_data = [
        (3, 6), (5.5, 8), (13.3, 8), (15.8, 6)
    ]
    for x, h in pillar_data:
        draw_rect(x, 3, 1.2, h, fill=False)
        draw_line(x + 0.6, 3, x + 0.6, 3 + h)  # middle line
    
    # Middle Pillar
    draw_rect(9.2, 3, 1.6, 8, fill=False)
    draw_line(9.2 + 0.8, 3, 9.2 + 0.8, 11)
    
    # Slanted upper frame
    vertices = [
        [9.2, 11],
        [10.8, 11],
        [11.3, 14],
        [9.7, 14]
    ]
    draw_polygon(vertices, fill=False)
    
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Shahid Minar OpenGL")
    
    glClearColor(1,1,1,1)  # white background
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 20, 0, 15)
    
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    from math import sin, cos
    main()