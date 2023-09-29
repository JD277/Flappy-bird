# Imorting pygame
import pygame
import time

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

    # Filling the window with color
    screen.fill('#0070ff')

    # Drawing the bg image
    screen.blit(bg_surf,bg_rect)

    # Animating the background
    bg_animation(dt)
    #   Updating the game
    pygame.display.update()

pygame.quit()