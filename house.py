from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    # Rectangle
    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)
    glVertex2f( 0.5, -0.5)
    glVertex2f( 0.5,  0.1)
    glVertex2f(-0.5,  0.1)
    glEnd()

    # Triangle
    glColor3f(0.8, 0.3, 0.3)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.6, 0.1)
    glVertex2f( 0.6, 0.1)
    glVertex2f( 0.0, 0.6)
    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Simple Object using GLUT")

    glClearColor(1, 1, 1, 1)
    gluOrtho2D(-1, 1, -1, 1)

    glutDisplayFunc(draw)
    glutMainLoop()

main()