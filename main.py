"""


Welcome to: Tricky Treats

ciss145 - Intro to Python programming
Final game project
Dec 8, 2017

By: Karissa Brickey


"""

#--------------------------------------------------------------------------#
# --- Setting up the basics.
#--------------------------------------------------------------------------#

#Import function libraries.
import pygame
import random
 
# Define constants (colors and screen width/ height)
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
PURPLE   = ( 180,  69, 225)
ORANGE   = ( 255, 110,   0)
BACKGROUND = (20,   0,   0)
BACKGROUND_FILL = (15,   0,   0)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

# Initialize pygame.
pygame.init()

#--------------------------------------------------------------------------#

# Set screen size and display window.
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

# Display game screen caption.
pygame.display.set_caption("·.·´¯`·.· Tricky Treats ·.·´¯`·.·")

# Set font formatting.
font = pygame.font.SysFont('Calibri', 55, True, False)
font1 = pygame.font.SysFont('Calibri', 20, True, False)
font2 = pygame.font.SysFont('Calibri', 50, True, False)
font3 = pygame.font.SysFont('Calibri', 35, True, False)

# Load background image.
background_image = pygame.image.load("hand_trees.jpg").convert()

# Load character images.
main_char_image = pygame.image.load("main_char.png").convert()
main_char_image.set_colorkey(BLACK)

cat_char_image = pygame.image.load("cat_char.png").convert()
cat_char_image.set_colorkey(BLACK)

wolf_char_image = pygame.image.load("wolf_char.png").convert()
wolf_char_image.set_colorkey(BLACK)

ghost_char_image = pygame.image.load("ghost_char.png").convert()
ghost_char_image.set_colorkey(BLACK)

# Load candy images.
candy_image = pygame.image.load("purple_candy.png").convert()
candy_image.set_colorkey(BLACK)

# Load music file.
pygame.mixer.music.load('tricky_treats_soundtrack.wav')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)

#--------------------------------------------------------------------------#
# --- Class definitions.
#--------------------------------------------------------------------------#

class Candy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
    
        # Assign candy image to object.
        self.image = candy_image
        self.rect = self.image.get_rect()
        
        # Assign x and y values to object.
        self.rect.x = random.randrange(0,650)
        self.rect.y = random.randrange(230,550)

#--------------------------------------------------------------------------#

class Cat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # Assign cat image to object.
        self.image = cat_char_image
        self.rect = self.image.get_rect()

    # The following methods specify unique screen locations of each object.
    def x1(self):
        self.rect.x = random.randrange(-80,-50)

    def x2(self):
        self.rect.x = -300

    def x3(self):
        self.rect.x = -590
        
    def y1(self):
        self.rect.y = random.randrange(300,330)

    def y2(self):
        self.rect.y = random.randrange(480,520)

    # Reset image to proper side of screen.
    def reset_pos(self):
        self.rect.x = -50
        
    def update(self):
        # Draw object (moving from left to right across screen).
        self.rect.x += 2

        # Reset object position to left side of screen if has moved off right
        # side of screen.
        if self.rect.x > 700:
            self.reset_pos()

#--------------------------------------------------------------------------#

class Wolf(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # Assign wolf image to object.
        self.image = wolf_char_image
        self.rect = self.image.get_rect()

    # The following methods specify unique screen locations of each object.
    def x1(self):
        self.rect.x = random.randrange(750,780)

    def x2(self):
        self.rect.x = random.randrange(900,1000)

    def x3(self):
        self.rect.x = 1200

    def x4(self):
        self.rect.x = 1400
        
    def y1(self):
        self.rect.y = random.randrange(235,260)

    def y2(self):
        self.rect.y = random.randrange(380,420)

    # Reset image to proper side of screen.
    def reset_pos(self):
        self.rect.x = 750
        
    def update(self):
        # Draw object (moving from right to left across screen).
        self.rect.x -= 2

        # Reset object position to right side of screen if has moved off left
        # side of screen.
        if self.rect.x < -50:
            self.reset_pos()

#--------------------------------------------------------------------------#

class Ghost(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # Assign ghost image to object.
        self.image = ghost_char_image
        self.rect = self.image.get_rect()
        self.rect.x = -50
        self.rect.y = random.randrange(270, 530)

    # Reset image to proper side of screen.
    def reset_pos(self):
        self.rect.x = -50
        self.rect.y = random.randrange(270, 530)
        
    def update(self):
        self.rect.x += 4

        # Reset object position to left side of screen if has moved off right
        # side of screen.
        if self.rect.x > 700:
            self.reset_pos()

#--------------------------------------------------------------------------#

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Assign player image to object.
        self.image = main_char_image
        self.rect = self.image.get_rect()
        
        # Current position
        self.rect.x = 10
        self.rect.y = 200
    
    def update(self):
        # Move the object according to the speed vector.
        self.rect.x += x_speed
        self.rect.y += y_speed

        # Check x bounds of player position.
        if (self.rect.x <= 0):
            self.rect.x = 0
        elif (self.rect.x >= 657):
            self.rect.x = 657

        # Check y bounds of player position.
        if (self.rect.y <= 180):
            self.rect.y = 180
        elif (self.rect.y >= 520):
            self.rect.y = 520


#******************************************************************************#
#*	             Display Game Screen & Begin Program	    	      *#
#******************************************************************************#

# Loop until the user clicks the close button.
running = True
while running:

    # Display main menu, set play game and show game-over screen to false.
    main = True
    instructions = False
    game = False
    game_over = False

    # Make sure music is not playing.
    pygame.mixer.music.stop()

    #--------------------------------------------------------------------------#
    # --- Display main menu.
    #--------------------------------------------------------------------------#
    while main:
        
        # Set up background image.
        screen.fill(BACKGROUND)
        screen.blit(background_image, [-100,-182])
        pygame.draw.line(screen, BACKGROUND_FILL, [570, 275], [700, 275], 20)
        pygame.draw.line(screen, BACKGROUND, [570, 292], [700, 292], 20)

        # Print game title.
        text = font1.render("W  E  L  C  O  M  E     T  O",True,ORANGE)
        screen.blit(text, [245, 240])
        pygame.draw.line(screen, WHITE, [0, 270], [700, 270], 3)
        text = font.render("·.·´¯`·.·",True,ORANGE)
        screen.blit(text, [30, 300])
        text = font.render(" TRICKY TREATS ",True,PURPLE)
        screen.blit(text, [167, 300])
        text = font.render("·.·´¯`·.·",True,ORANGE)
        screen.blit(text, [525, 300])
        pygame.draw.line(screen, WHITE, [0, 375], [700, 375], 3)

        # Print game options.
        text = font3.render("Click To Play", True, GREEN)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x -2, text_y +150])
        text1 = font3.render("Press ENTER To View Instructions", True, GREEN)
        text1_rect = text.get_rect()
        text1_x = screen.get_width() / 2 - text1_rect.width / 2
        text1_y = screen.get_height() / 2 - text1_rect.height / 2
        screen.blit(text1, [text1_x - 150, text1_y + 210])

        # --- Get user input for quit or play game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                main = False
                game = True
            elif event.type == pygame.KEYDOWN:
                main = False
                instructions = True

        # Update the screen.
        pygame.display.flip()

    #--------------------------------------------------------------------------#
    # --- Display instruction menu.
    #--------------------------------------------------------------------------#
    while instructions:
        
        # --- Set up background.
        screen.fill(BACKGROUND)

        # Print navigation instructions.
        pygame.draw.line(screen, WHITE, [0, 23], [700, 23], 3)
        text = font3.render("Press ENTER To Return To Main Menu", True, ORANGE)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y - 235])
        pygame.draw.line(screen, WHITE, [0, 100], [700, 100], 3)

        # Print game rules.
        text = font1.render("-  Navigate your character (pictured to the right) using the left, right,", True, GREEN)
        screen.blit(text, [10, 140])
        text = font1.render("   up, and down arrow keys on your keyboard.", True, GREEN)
        screen.blit(text, [10, 160])
        screen.blit(main_char_image, [600, 130])
        
        text = font1.render("-  There is a 'safe zone' where enemies cannot reach you at the top of your", True, GREEN)
        screen.blit(text, [10, 210])
        text = font1.render("   game screen.", True, GREEN)
        screen.blit(text, [10, 230])

        text = font1.render("-  Your goal is to earn as many points as possible before time runs out ", True, GREEN)
        screen.blit(text, [10, 280])
        text = font1.render("   (you have 35 seconds). The highest possible score is 150.", True, GREEN)
        screen.blit(text, [10, 300])

        text = font1.render("-  Points are earned by collecting the purple candy on the screen", True, GREEN)
        screen.blit(text, [10, 350])
        text = font1.render("   (pictured to the right). Each piece is worth 3 points.", True, GREEN)
        screen.blit(text, [10, 370])
        screen.blit(candy_image, [595, 350])

        text = font1.render("-  Avoid the cats and wolves: they steal your candy and you lose 10 points", True, GREEN)
        screen.blit(text, [10, 420])
        text = font1.render("   each time you hit one.", True, GREEN)
        screen.blit(text, [10, 440])

        text = font1.render("-  DEFINITELY watch out for that orange and white ghost flying around- if", True, GREEN)
        screen.blit(text, [10, 490])
        text = font1.render("   you hit him, you automatically die!", True, GREEN)
        screen.blit(text, [10, 510])

        # Print credits :D
        text = font3.render("·.·´¯`·.·",True,ORANGE)
        screen.blit(text, [100, 550])
        text = font1.render("Game Creator:  Karissa Brickey ", True, PURPLE)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y + 270])
        text = font3.render("·.·´¯`·.·",True,ORANGE)
        screen.blit(text, [500, 550])

        # --- Get user input for quit or play game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instructions = False
                running = False
            elif event.type == pygame.KEYDOWN:
                main = True
                instructions = False

        # Update the screen.
        pygame.display.flip()

    #--------------------------------------------------------------------------#
    # --- Initialize all game characters, score, time, and music for new game.
    #--------------------------------------------------------------------------#

    # Set frame rate and timer.
    clock = pygame.time.Clock()
    frame_count = 0
    frame_rate = 60
    start_time = 35

    # Speed in pixels per frame (moving main character with keyboard keys).
    x_speed = 0
    y_speed = 0

    # Create score variable.
    score = 0

    #--------------------------------------------------------------------------#
    # --- Organize sprites (characters).
    #--------------------------------------------------------------------------#

    # Create list of all candy objects.
    candy_list = pygame.sprite.Group()

    # Create list of all opponent objects.
    enemy_list = pygame.sprite.Group()

    # Create list of ghost objects.
    ghost_list = pygame.sprite.Group()

    # Create list of all game objects.
    all_sprites_list = pygame.sprite.Group()

    # --- Instantiate 40 candy sprites.
    for i in range(50):
        candy = Candy()
     
        # Add the candy sprite to list of candy objects.
        candy_list.add(candy)
        #all_sprites_list.add(candy)

    # --- Instantiate 3 enemy (cat) sprites.
    for i in range(3):
        cat_enemy = Cat()
        if i == 1:
            cat_enemy.y1()
            cat_enemy.x1()
        elif i == 2:
            cat_enemy.y2()
            cat_enemy.x2()
        else:
            cat_enemy.y2()
            cat_enemy.x3()
     
        # Add the candy sprite to list of candy objects.
        enemy_list.add(cat_enemy)
        all_sprites_list.add(cat_enemy)

    # --- Instantiate 3 enemy (wolf) sprites.
    for i in range(4):
        wolf_enemy = Wolf()
        if i == 0:
            wolf_enemy.y1()
            wolf_enemy.x1()
        elif i == 1:
            wolf_enemy.y2()
            wolf_enemy.x2()
        elif i == 2:
            wolf_enemy.y1()
            wolf_enemy.x3()
        elif i == 3:
            wolf_enemy.y2()
            wolf_enemy.x4()
     
        # Add the candy sprite to list of candy objects.
        enemy_list.add(wolf_enemy)
        all_sprites_list.add(wolf_enemy)

    # --- Create ghost object.
    ghost = Ghost()
    ghost_list.add(ghost)
    all_sprites_list.add(ghost)

    # --- Create player object.
    player = Player()
    all_sprites_list.add(player)

    # Play music.
    pygame.mixer.music.play()
        
    #--------------------------------------------------------------------------#
    # --- Start game.
    #--------------------------------------------------------------------------#
    while game:
        
        # --- Main event loop
        for event in pygame.event.get():

            # User hit the X button:
            if event.type == pygame.QUIT:
                running = False
                game = False
                    
            # User pressed a key:
            elif event.type == pygame.KEYDOWN:
                # Determine if arrow key pressed. If so adjust speed of character.
                if event.key == pygame.K_LEFT:
                    x_speed = -3
                elif event.key == pygame.K_RIGHT:
                    x_speed = 3
                elif event.key == pygame.K_UP:
                    y_speed = -3
                elif event.key == pygame.K_DOWN:
                    y_speed = 3

            # User let up on a key:
            elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero (stop character
                # movement).
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_speed = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_speed = 0
                            
        #----------------------------------------------------------------------#
        # --- Game logic.
        #----------------------------------------------------------------------#
                
        all_sprites_list.update()

        # Determine candy collisions.
        candy_hit_list = pygame.sprite.spritecollide(player, candy_list, True)  
         
        # If candy is hit, add 3 to score.
        for item in candy_hit_list:
            score += 3

        # Determine enemy collisions.
        enemy_hit_list = pygame.sprite.spritecollide(player, enemy_list, False)  
         
        # If enemy is hit, substract 2 from score.
        for item in enemy_hit_list:
            if (frame_count % 45 == 0):
                score -= 10

        # Determine ghost collisions.
        ghost_hit_list = pygame.sprite.spritecollide(player, ghost_list, False)
        if (ghost_hit_list):
            game = False
            game_over = True

            # Stop the music.
            pygame.mixer.music.stop()

        #----------------------------------------------------------------------#
        # --- Drawing code.
        #----------------------------------------------------------------------#

        # Draw background elements.
        screen.fill(BACKGROUND)
        screen.blit(background_image, [-100,-182])
        pygame.draw.line(screen, BACKGROUND_FILL, [570, 275], [700, 275], 20)
        pygame.draw.line(screen, BACKGROUND, [570, 292], [700, 292], 20)
        pygame.draw.line(screen, BLACK, [0, 585], [700, 585], 25)

        # Draw candy.
        candy_list.draw(screen)
        
        # Draw characters.
        all_sprites_list.draw(screen)

        # Print score to screen.
        text = font1.render("Score: " + str(score), True, PURPLE)
        screen.blit(text, [10, 578])

        #----------------------------------------------------------------------#
        # --- Timer going down.
        #----------------------------------------------------------------------#

        # Calculate total seconds.
        total_seconds = start_time - (frame_count // frame_rate)
        if total_seconds <= 0:
            game = False
            game_over = True

            # Stop the music.
            pygame.mixer.music.stop()
 
        # Divide by 60 to get total minutes.
        minutes = total_seconds // 60
 
        # Use modulus (remainder) to get seconds.
        seconds = total_seconds % 60
 
        # Use string formatting to format in leading zeros.
        output_string = "Time:  {0:02}:{1:02}".format(minutes, seconds)
 
        # Print to screen.
        text = font1.render(output_string, True, PURPLE)
        screen.blit(text, [585, 578])

        # Update frame count.
        frame_count += 1

        # Update the screen.
        pygame.display.flip()

        # Limit frames per second.
        clock.tick(frame_rate)

    #--------------------------------------------------------------------------#
    # --- Display game over menu.
    #--------------------------------------------------------------------------#
    while game_over:
        
        # Draw game over, final score, & prompt for play again.
        text = font2.render("GAME OVER", True, GREEN)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2

        text1 = font3.render("Final Score: " + str(score), True, WHITE)
        text1_rect = text1.get_rect()
        text1_x = screen.get_width() / 2 - text_rect.width / 2
        text1_y = screen.get_height() / 2 - text_rect.height / 2

        text2 = font3.render("Click To Play Again", True, GREEN)
        text2_rect = text2.get_rect()
        text2_x = screen.get_width() / 2 - text_rect.width / 2
        text2_y = screen.get_height() / 2 - text_rect.height / 2
        
        screen.blit(text, [text_x, text_y - 50])
        screen.blit(text1, [text1_x + 15, text1_y + 5])
        screen.blit(text2, [text2_x - 8, text2_y + 50])

        # Get user input for play again or quit game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game_over = False
                running = True

        # Update the screen.
        pygame.display.flip()
     
 #--------------------------------------------------------------------------#
 
# Close the window and quit.
pygame.quit()

