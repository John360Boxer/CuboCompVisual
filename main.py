import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from solid import Cube
from transformations import rotate, translate, scale
from textures import load_textures

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    
    cube = Cube()
    load_textures(cube)

    # Parâmetros de transformação
    angle_y = 0
    angle_x = 0
    angle_z = 0
    tx, ty, tz = 0, 0, 0
    sx, sy, sz = 1, 1, 1

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)  # Limita a taxa de quadros a 60 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Obtém o estado das teclas
        keys = pygame.key.get_pressed()

        if keys[K_LEFT]:
            angle_y += 1
        if keys[K_RIGHT]:
            angle_y -= 1
        if keys[K_UP]:
            angle_x += 1
        if keys[K_DOWN]:
            angle_x -= 1
        if keys[K_w]:
            ty += 0.02
        if keys[K_s]:
            ty -= 0.02
        if keys[K_a]:
            tx -= 0.02
        if keys[K_d]:
            tx += 0.02
        if keys[K_q]:
            sx *= 1.01
            sy *= 1.01
            sz *= 1.01
        if keys[K_e]:
            sx /= 1.01
            sy /= 1.01
            sz /= 1.01
        if keys[K_i]:  # Novo comando para rotação ao redor do eixo Z
            angle_z += 1
        if keys[K_k]:  # Novo comando para rotação ao redor do eixo Z
            angle_z -= 1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        translate(tx, ty, tz)
        rotate(angle_x, 'x')
        rotate(angle_y, 'y')
        rotate(angle_z, 'z')
        scale(sx, sy, sz)

        cube.draw()
        pygame.display.flip()

if __name__ == "__main__":
    main()
