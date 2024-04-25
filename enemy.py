import pygame

class ZombieEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y, MAX_HP_base:int=100, name:str='', width=25, heigth=25):
        super().__init__()
        #self.image = pygame.image.load('images/zombie.png')
        # Crear un rectángulo cyan en lugar de cargar una imagen
        self.image = pygame.Surface((width, heigth)) # Tamaño del rectángulo
        self.rgb = (0, 255, 255) # Color Cyan
        self.image.fill(self.rgb) # Se dibuja/pinta aquí
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_change = 0
        self.MAX_HP_base = MAX_HP_base  # df_ini_stat['HP'][self.dualtype]
        self.MAX_HP = self.MAX_HP_base
        self.HP = self.MAX_HP_base
        self.type = 'enemy'
        if name == 'MP':
            self.Atq_base = 7
        elif name == 'Guard Hound':
            self.Atq_base = 14
        elif name == '1st Ray':
            self.Atq_base = 5
        else:
            self.Atq_base = 10

        self.alive = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def attack(self, player):
        player.HP -= self.Atq_base
        if player.HP <= 0:
            player.alive = False