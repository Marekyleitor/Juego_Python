import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, MAX_HP_base=100, width=25, heigth=25):
        super().__init__()
        #self.image = pygame.image.load('images/character.png')
        # Crear un rectángulo blanco en lugar de cargar una imagen
        self.image = pygame.Surface((width, heigth)) # Tamaño del rectángulo
        self.rgb = (255, 255, 255) # Color blanco
        self.image.fill(self.rgb) # Se dibuja/pinta aquí
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_change = 0
        self.MAX_HP_base = MAX_HP_base # df_ini_stat['HP'][self.dualtype]
        self.MAX_HP = self.MAX_HP_base
        self.HP = self.MAX_HP_base
        # self.health = health
        # self.max_health = self.MAX_HP_base # + o - ciertos atributos
        self.type = 'player'

        self.Lv = 6
        self.XP = 610
        self.alive = True
        self.MAX_LV = 99 # df_XP_Table.shape[0] # 99
        self.XP_limit0 = 372 # xp_Lv(self.Lv, self.MAX_LV)
        self.XP_limit1 = 616 # xp_Lv(self.Lv + 1, self.MAX_LV)
        # self.weapon = arma_inicial(self.tipo)
        self.Atq_base = 17 # self.FRZ_total // 2

    def update(self):
        now = pg.time.get_ticks()
        if now - self.start_time > self.time_limit:
            self.frame += 1  # Incrementar el índice del fotograma
            self.frame %= len(IMAGES)  # Mantener el índice dentro del rango
            self.image = IMAGES[self.frame]  # Cambiar la imagen
            self.start_time = now  # Actualizar el tiempo de inicio

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def attack(self, enemy):
        enemy.HP -= self.Atq_base
        if enemy.HP <= 0:
            enemy.alive = False