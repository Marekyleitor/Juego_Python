import pygame
from pygame.sprite import Sprite, Group
from pygame.locals import *
import sys
from player import Player
from enemy import ZombieEnemy

##### python myGame.py #####

# Inicializar Pygame
pygame.init()

# Configurar la ventana del juego
screen = pygame.display.set_mode((800, 600))

# Crear instancias de las clases
player = Player(400, 300, 314)
zombie1 = ZombieEnemy(200, 100, 30, 'MP') # MP
zombie2 = ZombieEnemy(300, 250, 42, 'Guard Hound') # Guard Hound
zombie3 = ZombieEnemy(700, 150, 18, '1st Ray') # 1st Ray

# Crear un temporizador para la animación de colisión
COLLISION_ANIMATION_DURATION = 500  # Duración en milisegundos
#  collision_timer = pygame.time.set_timer(USEREVENT, COLLISION_ANIMATION_DURATION)

# Variables de movimiento y atributos del personaje
steps = 25 # Cuántos píxeles se moverán el personaje y enemigos
mini_steps = 5 # Cuántos píxeles se moverá el personaje

# Array de enemigos
enemies = [zombie1, zombie2, zombie3]

# Crear un objeto de fuente
font = pygame.font.Font(None, 36)

def display_update():
    # Limpiar la pantalla
    screen.fill((0, 0, 0))

    # Dibujar el personaje
    #pygame.draw.rect(screen, player.rgb, pygame.Rect(player.rect.x, player.rect.y, 50, 50))
    player.draw(screen)
    print(f'player.rect.x: {player.rect.x}')
    print(f'player.rect.y: {player.rect.y}')

    # Renderizar la vida del personaje
    local_health_text = font.render(f"Vida: {player.HP}/{player.MAX_HP}", True, (255, 255, 255))
    screen.blit(local_health_text, (10, 10))

    # Dibujar a los enemigos
    for i in range(len(enemies)):
        if enemies[i].alive:
            #pygame.draw.rect(screen, enemies[i].rgb, pygame.Rect(enemies[i].rect.x, enemies[i].rect.y, 50, 50))
            enemies[i].draw(screen)

    pygame.display.flip()

def player_attack_enemy_counter_attack(player, enemy, move_to, way, mini_steps):
    player_attack_animation(player, enemies[i], move_to, way, mini_steps)
    if way == 'go':
        player.attack(enemies[i])
    if enemies[i].alive:
        enemy_counter_attack_animation(player, enemies[i], move_to, way, mini_steps)
        if way == 'go':
            enemies[i].attack(player)


def player_attack_animation(player, enemy, move_to, way, mini_steps):
    a = 1 if way == 'go' else -1
    if move_to == 'LEFT':
        player.rect.x -= mini_steps * a
    if move_to == 'RIGHT':
        player.rect.x += mini_steps * a
    if move_to == 'UP':
        player.rect.y -= mini_steps * a
    if move_to == 'DOWN':
        player.rect.y += mini_steps * a
    display_update()
    pygame.time.wait(50)

def enemy_counter_attack_animation(player, enemy, move_to, way, mini_steps):
    a = 1 if way == 'go' else -1
    if move_to == 'LEFT':
        enemy.rect.x += mini_steps * a
    if move_to == 'RIGHT':
        enemy.rect.x -= mini_steps * a
    if move_to == 'UP':
        enemy.rect.y += mini_steps * a
    if move_to == 'DOWN':
        enemy.rect.y -= mini_steps * a
    display_update()
    pygame.time.wait(50)

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        move_to = None
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == USEREVENT:
            # Aquí puedes manejar la lógica de la animación de colisión
            # Por ejemplo, cambiar la posición de los objetos y luego volver a su posición original
            pass
        elif event.type == pygame.KEYDOWN:
            # Crear un rectángulo temporal para la posición futura del jugador
            future_player_rect = player.rect.copy()
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                future_player_rect.x -= steps
                move_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                future_player_rect.x += steps
                move_to = 'RIGHT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                future_player_rect.y -= steps
                move_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                future_player_rect.y += steps
                move_to = 'DOWN'

            # Verificar si el movimiento propuesto resultaría en una colisión
            hubo_colision = False
            for i in range(len(enemies)):
                if enemies[i].alive and future_player_rect.colliderect(enemies[i].rect):
                    # Realizar la animación de colisión en lugar de mover el jugador
                    # Mover el jugador y el enemigo 10 píxeles hacia arriba y hacia abajo

                    player_attack_enemy_counter_attack(player, enemies[i], move_to, 'go', mini_steps)

                    # Actualizar la pantalla para mostrar la animación
                    #display_update()
                    # Esperar un poco para que la animación sea visible
                    #pygame.time.wait(100)
                    # Regresar a la posición original

                    player_attack_enemy_counter_attack(player, enemies[i], move_to, 'back', mini_steps)

                    # Actualización de vida
                    ####player.attack(enemies[i])
                    print(f"enemies[i].HP: {enemies[i].HP}")
                    print(f"enemies[i].alive: {enemies[i].alive}")
                    ####if enemies[i].alive:
                    ####    enemies[i].attack(player)

                    display_update()
                    hubo_colision = True
                    break # para salir del for
                    #pass
            if not hubo_colision:
                player.rect = future_player_rect

    # Limpiar la pantalla
    screen.fill((0, 0, 0))

    # Dibujar el personaje
    #pygame.draw.rect(screen, player.rgb, pygame.Rect(player.rect.x, player.rect.y, 25, 25))
    player.draw(screen)

    # Renderizar la vida del personaje
    health_text = font.render(f"Vida: {player.HP}/{player.MAX_HP}", True, (255, 255, 255))
    screen.blit(health_text, (10, 10))

    # Dibujar a los enemigos
    for i in range(len(enemies)):
        if enemies[i].alive:
            #pygame.draw.rect(screen, enemies[i].rgb, pygame.Rect(enemies[i].rect.x, enemies[i].rect.y, 25, 25))
            enemies[i].draw(screen)

    # Detectar colisiones
    if pygame.sprite.spritecollideany(player, enemies):
        #print("Colisión con enemigo")
        #player.HP -= 10
        pass
    #if pygame.sprite.spritecollideany(player, walls):
    #    print("Colisión con pared")

    # Actualizar la pantalla
    pygame.display.flip()