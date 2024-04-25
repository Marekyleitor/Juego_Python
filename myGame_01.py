import pygame as pg
from pygame.sprite import Sprite, Group
from pygame.locals import *
import sys
from player import Player
from enemy import ZombieEnemy

##### python myGame_01.py #####

# Cargar las imágenes para la animación
IMAGE1 = pg.image.load('C:/Users/Documentos/Python_Projects/Juego_Python/images/character.png')
IMAGE2 = pg.image.load('C:/Users/Documentos/Python_Projects/Juego_Python/images/MP.png')
IMAGE3 = pg.image.load('C:/Users/Documentos/Python_Projects/Juego_Python/images/zombie.png')
IMAGES = [IMAGE1, IMAGE2, IMAGE3]

class AnimatedEntity(pg.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.frame = 0 # Índice del fotograma actual
        self.image = IMAGES[self.frame] # Establecer la imagen al primer fotograma
        self.rect = self.image.get_rect(center=pos)
        self.start_time = pg.time.get_ticks() # Tiempo de inicio de la animación
        self.time_limit = 300 # Límite de tiempo en milisegundos para cambiar de fotograma

    def update(self):
        now = pg.time.get_ticks()
        if now - self.start_time > self.time_limit:
            self.frame += 1 # Incrementar el índice del fotograma
            self.frame %= len(IMAGES) # Mantener el índice dentro del rango
            self.image = IMAGES[self.frame] # Cambiar la imagen
            self.start_time = now # Actualizar el tiempo de inicio

# Inicializar Pygame y crear la pantalla
pg.init()
screen = pg.display.set_mode((960, 720))
clock = pg.time.Clock()

# Crear una instancia de la entidad animada
entity = AnimatedEntity((200, 200))

# Bucle principal del juego
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Actualizar la entidad animada
    entity.update()

    # Dibujar la entidad en la pantalla
    screen.fill((30, 30, 30))
    screen.blit(entity.image, entity.rect)

    pg.display.flip()
    clock.tick(30) # Limitar la velocidad del bucle a 30 FPS

pg.quit()