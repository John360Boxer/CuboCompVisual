from OpenGL.GL import *
from PIL import Image

def load_textures(cube):
    for i in range(6):
        glBindTexture(GL_TEXTURE_2D, cube.texture_ids[i])
        img = Image.open(f'texture_{i}.png')
        
        # Inverte as texturas das faces 1, 4, 5 e 6, que estão ao contrário
        if i in [0, 3, 4, 5]:
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
        
        img = img.convert("RGB")
        img_data = img.tobytes("raw", "RGB", 0, -1)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glBindTexture(GL_TEXTURE_2D, 0)  # Desvincule a textura após carregar
