import pygame
import time
import random

# initializing the pygame module
pygame.init()

# Defining colors that will be used in the game
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Setting dimensions of game window
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Initializing clock to control game frame rate
clock = pygame.time.Clock()

# Setting block and speed to determine size and speed of the snake
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont(None, 30)

# function to format messages displayed to user 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    # initial position of the snake
    x1 = dis_width / 2
    y1 = dis_height / 2

    # change in position of the snake
    x1_change = 0
    y1_change = 0

    # list to keep track of snake body
    snake_List = []
    Length_of_snake = 1

    # ransdom initial position of food
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    score = 0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
            
        # event handling: capturing user input and direction changes for the snake
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # boundary checking: checking if the snake has hit one of the boundaries
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # chanfing position of snake based on user input
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        
        #adding snake head coordinated to snake list (list of all body segments)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # make sure that length of the snake remains constant as long as snake has not eaten food
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Detecting snake collision with its own body
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Drawing the snake on screen
        for block in snake_List:
            pygame.draw.rect(dis, black, [block[0], block[1], snake_block, snake_block])

        pygame.display.update()
        
        # Checking if the snake has successfully found and eaten food
        if x1 == foodx and y1 == foody:

          # generating a new random position for food to be placed
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

            # increasing the length of the snake by 1
            Length_of_snake += 1

            # increasing the score by 1
            score += 1

        # Display Score
        score_font = pygame.font.SysFont(None, 25)
        value = score_font.render("Your Score: " + str(score), True, yellow)
        dis.blit(value, [0, 0])

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
