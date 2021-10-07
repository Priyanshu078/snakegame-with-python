import pygame
import random
pygame.init()

#colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# game screen
screenHeight = 700
screenWidth = 900
gameWindow = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Snakes")

# game variables
exit_game = False
gameOver = False
score = 0
snake_x = 55
snake_y = 55
snake_size = 30
speed_x = 0
speed_y = 0
food_x = random.randint(20, int(screenWidth/1.5))
food_y = random.randint(20, int(screenHeight/1.5))
increaseSpeed = 10
snake_list = []
snake_length = 1
fps = 50
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def printTextOnScreen(text, color, x, y):
    screenText = font.render(text,True,color)
    gameWindow.blit(screenText, [x, y])


#gameloop
def gameLoop():
    exit_game = False
    gameOver = False
    score = 0
    snake_x = 55
    snake_y = 55
    snake_size = 30
    speed_x = 0
    speed_y = 0
    food_x = random.randint(20, int(screenWidth / 1.5))
    food_y = random.randint(20, int(screenHeight / 1.5))
    increaseSpeed = 10
    snake_list = []
    snake_length = 1
    fps = 40
    clock = pygame.time.Clock()

    while not exit_game:
        if gameOver == True:
            gameWindow.fill(white)
            printTextOnScreen("GameOver! Press enter to play again",red , 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameLoop()


        else:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        speed_y = increaseSpeed
                        speed_x = 0

                    if event.key == pygame.K_RIGHT:
                        speed_x = increaseSpeed
                        speed_y = 0

                    if event.key == pygame.K_LEFT:
                        speed_x = -increaseSpeed
                        speed_y = 0

                    if event.key == pygame.K_UP:
                        speed_y = -increaseSpeed
                        speed_x = 0

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score += 1
                food_x = random.randint(20, int(screenWidth / 1.5))
                food_y = random.randint(20, int(screenHeight / 1.5))
                snake_length += 2


            snake_x += speed_x
            snake_y += speed_y
            gameWindow.fill(white)
            printTextOnScreen("Score : " + str(score), red, 5, 5)
            plot_snake(gameWindow, black, snake_list, snake_size)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if(len(snake_list) > snake_length):
                del snake_list[0]

            if snake_x < 0 or snake_x > screenWidth or snake_y < 0 or snake_y > screenHeight:
                gameOver = True

            if head in snake_list[:-1]:
                gameOver = True

            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

        pygame.display.update()
        clock.tick(fps)

gameLoop()
pygame.quit()
quit()
