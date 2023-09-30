# Imorting pygame
import pygame
import time
import random
pygame.init()

# Creating the window 
screen = pygame.display.set_mode((400,600))

# Adding the title to the window
pygame.display.set_caption('Travelling')

# Adding the icon to the window
icon = pygame.image.load('./Graphics/Player.png')
pygame.display.set_icon(icon)

# Adding the background to the window
bg_surf = pygame.image.load('./Graphics/bg.png').convert_alpha()
bg_rect = bg_surf.get_rect(topleft = (0,0))
movement = pygame.math.Vector2(bg_rect.topleft)
bg_speed = 600

def bg_animation(dt):
    global bg_rect, movement
    movement.x -= bg_speed * dt
    if bg_rect.left <= -960:
        movement.x = -100
    bg_rect.x = movement.x
            
# Player setup
player_surf = pygame.image.load('./Graphics/Player.png').convert_alpha()
player_rect = player_surf.get_rect(center = (150,300))
player_mov = pygame.math.Vector2(player_rect.topleft)
player_gravity = 1


def player_fall(dt):
    global player_rect, player_gravity, player_surf
    # Setting the player gravity increment
    player_gravity += 10

    # Animating the player gravity  with delta time
    player_mov.y += player_gravity * dt
    
    # Applying the animations values to the sprite
    player_rect.y = round(player_mov.y)

# Enemies setup
enemy_type = random.randint(0,1)
if enemy_type == 1:
    obstacle = './Graphics/1.png'
    y_pos = 500
    enemy_surf = pygame.image.load(obstacle)
else:
    obstacle = './Graphics/0.png'
    y_pos = 100
    enemy_surf = pygame.image.load(obstacle)
    enemy_surf = pygame.transform.rotozoom(enemy_surf,90,1)
    

enemy_surf = pygame.image.load(obstacle)
enemy_rect = enemy_surf.get_rect(midleft = (400,y_pos))
enemy_movement = pygame.math.Vector2(enemy_rect.topleft)
enemy_speed = 400

enemy_event = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_event, 900)
# While condition
running = True 

previus_time = time.time()
clock = pygame.time.Clock()
# While loop
while running:
    clock.tick(60)
    # Adding Delta time to control the framerate
    dt = time.time() - previus_time
    previus_time = time.time()
    # For loop events
    for event in pygame.event.get():

        # Event for closing the game window
        if event.type == pygame.QUIT:
            running = False
        # Event for fly 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player_gravity = -200
        if event.type == enemy_event:
            pass


    # Filling the window with color
    screen.fill('#0070ff')

    # Drawing the bg image
    screen.blit(bg_surf,bg_rect)

    # Animating the background
    bg_animation(dt)

    # Drawing the player
    screen.blit(player_surf,player_rect)
    #player_fall(dt)

    screen.blit(enemy_surf,enemy_rect)
    enemy_movement.x -= enemy_speed * dt
    enemy_rect.x = enemy_movement.x
    #   Updating the game
    pygame.display.update()

pygame.quit()