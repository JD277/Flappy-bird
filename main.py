# Imorting pygame
import pygame
import time
import random
pygame.init()

# Creating the window 
screen = pygame.display.set_mode((400,550))

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

# Enemies that come from the ground
enemy_type = random.randint(0,1)
enemy_rect = []
enemy_movement = []
enemy_speed = 400
enemy_surf1 = pygame.image.load('./Graphics/1.png')
enemy_surf1 = pygame.transform.scale(enemy_surf1,(108*1.2, 239*1.2))

def create_enemy1():
    global enemy_movement, enemy_rect, enemy_surf1
    y_pos = 450
    enemy_rect.append(enemy_surf1.get_rect(midleft = (400,y_pos)))
    enemy_movement.append(pygame.math.Vector2(enemy_rect[len(enemy_rect)- 1].topleft))

# Enemies that come from the sky
enemy_surf2 = pygame.image.load('./Graphics/0.png')
enemy_surf2 = pygame.transform.scale(enemy_surf2,(108*1.2, 239*1.2))
enemy_rect2 = []
enemy_movement2 = []

def create_enemy2():
    global enemy_movement2, enemy_rect2, enemy_surf2
    y_pos = 100
    enemy_rect2.append(enemy_surf2.get_rect(midleft = (400,y_pos)))
    enemy_movement2.append(pygame.math.Vector2(enemy_rect2[len(enemy_rect2)- 1].topleft))

# Enemy timer
enemy_event = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_event, 900)
# Scoring
text_font = pygame.font.Font('./Fonts/Origin.ttf',60)
start_time = 0
score = 0
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000)  - start_time
    score_surface = text_font.render(f'{current_time}', False, 'Black')
    score_rect = score_surface.get_rect(center = (200, 100))
    
    # Showing the score text 
    screen.blit(score_surface, score_rect)
    return current_time
# Menu objects
menuimg_surf = pygame.image.load('./Graphics/rocket.png')
menuimg_rect = menuimg_surf.get_rect(center = (200, 275))

menutext_surf = text_font.render('Traveling', False, 'White')
menutext_rect = menutext_surf.get_rect(center = (200,100))

menu_font = pygame.font.Font('./Fonts/Origin.ttf',20)
menutext_surf2 = menu_font.render('Press SPACE to start your travel', False, 'White')
menutext_rect2 = menutext_surf2.get_rect(center = (200,400))

# While condition
running = True 
# Game state
game_active = False
# Creating the clocks
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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and game_active == False:
            game_active = True
            start_time = int(pygame.time.get_ticks() / 1000) 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player_gravity = -200
        if event.type == enemy_event:
            enemy_type = random.randint(0,1)
            if enemy_type == 1:
                create_enemy1()
            
            elif enemy_type == 0:
                create_enemy2()
            
            
    # Filling the window with color
    screen.fill('#212323')

    if game_active:
        score = 0
        # Drawing the bg image
        screen.blit(bg_surf,bg_rect)

        # Animating the background
        bg_animation(dt)

        # Drawing the player
        screen.blit(player_surf,player_rect)
        player_fall(dt)


        # Drawing the enemies of the ground
        for a in range(len(enemy_rect)):
            screen.blit(enemy_surf1,enemy_rect[a])

            enemy_movement[a].x -= enemy_speed * dt
            enemy_rect[a].x = enemy_movement[a].x

        for b in enemy_rect:
            enemy_rect = [rectangle for rectangle in enemy_rect if rectangle.x > -250]

        for c in enemy_movement:
            enemy_movement = [move for move in enemy_movement if move.x > -250]
        
        # Drawing the enemies of the sky
        for d in range(len(enemy_rect2)):
            screen.blit(enemy_surf2,enemy_rect2[d])

            enemy_movement2[d].x -= enemy_speed * dt
            enemy_rect2[d].x = enemy_movement2[d].x

        for e in enemy_rect2:
            enemy_rect2 = [rectangle2 for rectangle2 in enemy_rect2 if rectangle2.x > -250]

        for d in enemy_movement2:
            enemy_movement2 = [move2 for move2 in enemy_movement2 if move2.x > -250]

        # Score
        score = display_score()

        if player_rect.collidelist(enemy_rect) != -1 or player_rect.collidelist(enemy_rect2) != -1 or player_rect.y >= 550:
            game_active = False
            enemy_movement.clear()
            enemy_movement2.clear()
            enemy_rect.clear()
            enemy_rect2.clear()
    else:
        screen.blit(menuimg_surf, menuimg_rect)
        screen.blit(menutext_surf, menutext_rect)
        screen.blit(menutext_surf2, menutext_rect2)
        
    #   Updating the game
    pygame.display.update()

pygame.quit()