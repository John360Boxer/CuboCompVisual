from OpenGL.GL import *

def rotate(angle, axis):
    if axis == 'x':
        glRotatef(angle, 1, 0, 0)
    elif axis == 'y':
        glRotatef(angle, 0, 1, 0)
    elif axis == 'z':
        glRotatef(angle, 0, 0, 1)

def translate(tx, ty, tz):
    glTranslatef(tx, ty, tz)

def scale(sx, sy, sz):
    glScalef(sx, sy, sz)
