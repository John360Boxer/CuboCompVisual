from OpenGL.GL import *

class Cube:
    def __init__(self):
        self.vertices = [
            [1, 1, -1],
            [1, -1, -1],
            [-1, -1, -1],
            [-1, 1, -1],
            [1, 1, 1],
            [1, -1, 1],
            [-1, -1, 1],
            [-1, 1, 1]
        ]
        self.faces = [
            (0, 1, 2, 3),
            (4, 5, 6, 7),
            (0, 4, 5, 1),
            (1, 5, 6, 2),
            (2, 6, 7, 3),
            (4, 0, 3, 7)
        ]
        self.texture_coords = [
            (0, 0),
            (1, 0),
            (1, 1),
            (0, 1)
        ]
        self.texture_ids = glGenTextures(6)  # Gere IDs de textura

    def draw(self):
        for i, face in enumerate(self.faces):
            glBindTexture(GL_TEXTURE_2D, self.texture_ids[i % 6])  # Vincule a textura
            glBegin(GL_QUADS)
            for j, vertex in enumerate(face):
                glTexCoord2fv(self.texture_coords[j % 4])
                glVertex3fv(self.vertices[vertex])
            glEnd()
        glBindTexture(GL_TEXTURE_2D, 0)  # Desvincule a textura após desenhar
