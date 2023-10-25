
import pygame
from random import randint

#Importing classes
from balls import Ball
from brick import Brick
from button import Button

#make arrow signaling direction
#make blocks have levels
#make ball powerup
#restart button

pygame.init()

#For screen resolution, when altered all objects will adjust accordingly
width = 540
height = 960

#Game parameters
velocity = 15
blocknum = 5
limit = 7

#Mechanic variables
start = 0
score = 0
topscore = 0
round = False
lose = False

#For scalability purposes
ave = (width + height)/2
ball_ratio = ave/35
fontsize1 = int(ave/20)
fontsize2 = int(ave/10)

#Defining Colors
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0, 0, 0)

# Opening new window
size = (width, height)
screen = pygame.display.set_mode((size))
pygame.display.set_caption("Project")

all_sprites_list = pygame.sprite.Group()

#To randomly place colored bricks across width of screen
all_bricks = pygame.sprite.Group()
def blocks(num):
    for i in range(num):
        chance = randint(0, 1)
        COLOR = (randint(10, 255), randint(10, 255), randint(10, 255))
        if chance == 1:
            brick = Brick(COLOR, width/blocknum, height/limit)
            brick.rect.x = 0 + i* width/blocknum
            brick.rect.y = fontsize1 + 6
            all_sprites_list.add(brick)
            all_bricks.add(brick)
blocks(blocknum)

#Defining Ball
ball = Ball(WHITE, ball_ratio, ball_ratio, width/2, height*0.95)
ball.reset(width)
all_sprites_list.add(ball)

#Defining Buttons
resetbutton = Button(BLACK,  width * 0.85, 0, 2 * fontsize1, fontsize1, 'Reset')
#retrybutton = Button(BLACK,  width/2, height * (3/8), 2 * fontsize1, fontsize1, 'Try Again')
#quitbutton = Button(BLACK,  width/2, height * (3/4), 2 * fontsize1, fontsize1, 'Quit Game')

carryOn = True
clock = pygame.time.Clock()

while carryOn:  
    for event in pygame.event.get(): 
        pos = pygame.mouse.get_pos()

        #When pressing close, exits program
        if event.type == pygame.QUIT: 
              carryOn = False 

        #To aim the ball
        if event.type == pygame.MOUSEBUTTONDOWN and round == False:
            round = True
            ball.movement(velocity)

        #For reset button to function
        if (event.type == pygame.MOUSEBUTTONDOWN) and (resetbutton.isOver(pos) == True) and (round == True):
            #I tried putting this into a function but it didn't work, so i simply repeated it later
            ball.die()
            for brick in all_bricks:
                brick.rect.y += height/limit
            blocks(blocknum)     
            all_sprites_list.add(ball)
            ball.reset(width)
            round = False
            score += 1
        """""        
        #For endgame buttons to function
        if (lose == True):
            if ((event.type == pygame.MOUSEBUTTONDOWN)) and (retrybutton.isOver(pos) == True):
                lose == False
                round = False
                score = 0
                for brick in all_bricks:
                    brick.kill()
                ball.reset(width)
                blocks(blocknum)
                carryOn == True
                all_sprites_list.draw(screen)
                pygame.display.flip()

            if ((event.type == pygame.MOUSEBUTTONDOWN)) and (quitbutton.isOver(pos) == True):
                pygame.time.wait(500)
                carryOn = False
        """""               
                
    all_sprites_list.update()

    #To update top score
    if topscore <= score:
        topscore = score


    #Bouncing Mechanic
    if ball.rect.x >= width:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y <= 0:
        ball.velocity[1] = -ball.velocity[1]

    #Disappearing ball when touching the bottom or no bricks left, reseting position (same as previous)
    if (ball.rect.y>= height - 10 or len(all_bricks) == 0) and lose == False:
        ball.die()
        for brick in all_bricks:
            brick.rect.y += height/limit          
        blocks(blocknum)     
        all_sprites_list.add(ball)
        ball.reset(width)
        round = False
        score += 1

    #Lose condition
    for brick in all_bricks:
        if brick.rect.y >= ((limit - 1)/limit) * (height - 38):
            round = True
            font = pygame.font.Font(None, fontsize2)
            text = font.render("GAME OVER", 1, RED)
            text_rect = text.get_rect(center=(width/2, height/2))
            screen.blit(text, text_rect)
            lose = True
                       
            pygame.display.flip()
            pygame.time.wait(2000) 
            carryOn = False
            
            
            
            
            

    #Destroys brick when ball touches
    brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
    for brick in brick_collision_list:
        ball.bounce()
        brick.kill()
        
    #Coloring screen
    screen.fill(BLACK)

    #Line over block spawn, ball is intended to go through the line, it is purely asthetic
    pygame.draw.line(screen, WHITE, [0, fontsize1 + 4], [width, fontsize1 + 4], 2)

    #Allows for acceleration of ball when taking too long, and reveals button to instantly progress if ball gets stuck
    if round == True:
        start = clock.tick()
        ball.speedup(start) 
        resetbutton.draw(screen, fontsize1, WHITE)


    #Display the score at the top left of the screen
    font = pygame.font.Font(None, fontsize1)
    text = font.render("Score: " + str(score) + " / Best: " + str(topscore), 1, WHITE)
    screen.blit(text, (20,10))



    #Shows all the sprites on the screen
    all_sprites_list.draw(screen)



    #if lose == True:
    #    retrybutton.draw(screen, fontsize1, WHITE)
    #    quitbutton.draw(screen, fontsize1, WHITE)

    pygame.display.flip()

    #Frame rate of program
    clock.tick(60)

#Stops program
pygame.quit()