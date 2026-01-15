import random
import pygame
import sys
import os
#use to acees bundle resource for pyinstaller
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
#initiation of pygame
pygame.mixer.init()
pygame.init()
#colours
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
#Game Window Size
screen_width=900
screen_height=600
# Game Window
gameWindow = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
# game title
pygame.display.set_caption("Snake-Game")
pygame.display.update()  # It updates the game window so that everything user drew becomes visible on screen
#background image
home=pygame.image.load(resource_path("snakehome.png"))
home=pygame.transform.scale(home,(screen_width,screen_height)).convert_alpha()

main=pygame.image.load(resource_path("snakebackground.jpg"))
main=pygame.transform.scale(main,(screen_width,screen_height)).convert_alpha()

end=pygame.image.load(resource_path("Snakeenddddddddddddddddd.png"))
end=pygame.transform.scale(end,(screen_width,screen_height)).convert_alpha()

apple=pygame.image.load(resource_path("apple.png"))
apple_size=20
apple=pygame.transform.scale(apple,(apple_size,apple_size)).convert_alpha()
#Write screen-text
def text_screen(text, colour, x, y):  # Used to show score inside the game
    screen_text = font.render(text, True, colour)
    gameWindow.blit(screen_text, [x, y])
#use to plot snake
def plot_snake(gameWindow,colour,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, colour, [x,y, snake_size, snake_size])
#use for welcome/home screen
def welcome():
   pygame.mixer.music.load(resource_path("02. Clair-Obscur.mp3"))
   pygame.mixer.music.play()
   exit_game = False
   while not exit_game:
       gameWindow.fill((200,200,240))
       gameWindow.blit(home,(0,0))
       text_screen("Welcome To Snake Game",white,220,70)
       text_screen("Press Enter To Continue",white,230,500)
       for event in pygame.event.get():
           if(event.type==pygame.QUIT):
               exit_game=True
               pygame.quit()
               sys.exit()
           if(event.type==pygame.KEYDOWN):
               if(event.key==pygame.K_RETURN):
                   gameloop()
       pygame.display.update()
       clock.tick(30)
#creating a game loop
def gameloop():
    # pygame.mixer.music.load("C:\\Users\\Admin\\Downloads\\01. Alicia.mp3")
    # pygame.mixer.music.play()
    r=random.randint(0,screen_width)
    while(r==(600 or 700)):
        r=random.randint(0,screen_width)
    snake_list = []
    snake_length = 1
    # snake body
    snake_x = 20
    snake_y = 20
    snake_size = 15
    # food body
    food_x = random.randint(0, screen_width // 2)
    food_y = random.randint(0, screen_height // 2)
    food_size = 10
    fps = 30
    score = 0
    snake_velox = 0
    snake_veloy = 0
    # Game variables
    exit_game = False
    game_over = False
    if(not os.path.exists("Highscore.txt")):
        with open("Highscore.txt","w") as f:
            f.write("0")
    with open("Highscore.txt","r") as f:
            Highscore=int(f.read())
    while not exit_game:
        if(game_over):
            with open("Highscore.txt","w") as f:
                f.write(str(Highscore))
            gameWindow.fill((200, 233, 240))
            gameWindow.blit(end,(0,0))
            text_screen("Press Enter To Restart",black,225,370)
            text_screen("Your Score:"+str(score*10),white,50,70)
            text_screen("Highscore:"+str(Highscore*10),white,580,70)
            for event in pygame.event.get():
                if (event.type==pygame.QUIT):
                    exit_game=True
                if (event.type==pygame.KEYDOWN):
                    if (event.key==pygame.K_RETURN):
                        pygame.mixer.music.load(resource_path("02. Clair-Obscur.mp3"))
                        pygame.mixer.music.play()
                        gameloop()

        else:
            for event in pygame.event.get():
                if(event.type==pygame.QUIT):#event.type keeps track of user inputs and if event.type ==pygame.Quit(user press the close window button) then the game closes
                    exit_game=True
                if(event.type==pygame.KEYDOWN):#pygame.keydown is used to detect key presses
                    if(event.key==pygame.K_RIGHT):#event.key stores which key was pressed in this case right arrow is presses
                        snake_velox=8
                        snake_veloy=0
                    if(event.key==pygame.K_DOWN):
                        snake_veloy=8
                        snake_velox=0
                    if(event.key==pygame.K_UP):
                        snake_veloy=-8
                        snake_velox=0
                    if(event.key==pygame.K_LEFT):
                        snake_velox=-8
                        snake_veloy=0
            if(abs(snake_x-food_x)<apple_size and abs(snake_y-food_y)<apple_size):#Collision/close proximity
                score=score+1
                snake_length=snake_length+1
                food_x = r
                food_y = random.randint(0, screen_height)
            #HighScore logic
            if score > Highscore:
                Highscore = score

            snake_x=snake_x + snake_velox
            snake_y=snake_y + snake_veloy
            gameWindow.fill((0,255,255))
            gameWindow.blit(main,(0,0))
            #Snake body increase
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if(len(snake_list)>snake_length):
                del snake_list[0]
            if (snake_x > screen_width or snake_x < 0 or snake_y > screen_height or snake_y < 0):
                pygame.mixer.music.load(resource_path("gameover.wav"))
                pygame.mixer.music.play()
                game_over = True
            if head in snake_list[:-1]:
                pygame.mixer.music.load(resource_path("gameover.wav"))
                pygame.mixer.music.play()
                game_over=True

            text_screen("Score:"+str(score*10),red,700,20)
            text_screen("Highscore:" + str(Highscore*10),red,600,50)
            gameWindow.blit(apple,(food_x,food_y))
            # pygame.draw.rect(gameWindow,red,[food_x,food_y,food_size,food_size])#makes the food for snake
            plot_snake(gameWindow,(0,255,0),snake_list,snake_size)#It draws a rectangle in colour black inside game window and takes the x and y size
        clock.tick(fps)
        pygame.display.update()
    pygame.quit()
    sys.exit()
welcome()
gameloop()