import pygame as pg
import random

pg.init()

window = pg.display.set_mode((1280, 720)) 

ship = pg.image.load('Asteroid Destroyer/Files/ship.png')
ship_pos = ship.get_rect(center = (640,360)) #center the ship in the screen
ship_speed = 5

background = pg.image.load('Asteroid Destroyer/Files/space.png')

laser = pg.image.load('Asteroid Destroyer/Files/laser.png')
laser_pos = laser.get_rect(center = (-100, -100))
new_laser = []

asteroid = pg.image.load('Asteroid Destroyer/Files/asteroid.png')
asteroid_pos = asteroid.get_rect(center = (-100, -100))
asteroid_timer = pg.event.custom_type()
new_asteroid = []
spawn_time = 3000
pg.time.set_timer(asteroid_timer, spawn_time)       #asteroid timer
random_x = random.randint(0, 1280)
random_y = random.randint(-100, 0)

font1 = pg.font.Font ('Asteroid Destroyer/Files/arcade font.TTF', 20)         #Font for score, lives, level
font2 = pg.font.Font ('Asteroid Destroyer/Files/arcade font.TTF', 45)         #GAME OVER FONT

score = 0
score_text = font1.render('Score: %i' %score, False, 'White')
score_text_pos = score_text.get_rect (midbottom = (640, 700))

level = 1
level_text = font1.render('Level: %i' %level, False, 'White')
level_text_pos = level_text.get_rect (midbottom = (80, 700))

lives = 3
lives_text = font1.render('Lives: %i' %lives, False, 'White')
lives_text_pos = lives_text.get_rect (midbottom = (1200, 700))

gameOver = font2.render('GAME OVER!', False, 'White')
gameOver_pos = gameOver.get_rect (center = (-200, -200))


clock = pg.time.Clock()

pg.display.set_caption ('Asteroid Destroyer')

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:      
            pg.quit()
            exit(0)
        if event.type == pg.KEYDOWN:                #laser shooter (done)
            if event.key == pg.K_SPACE:     #spacebar to shoot laser (done)
                laser_pos = laser.get_rect(midbottom = ship_pos.midtop)   
                new_laser.append(laser_pos) 
        if event.type == asteroid_timer:       #asteroid spawner (done)
            asteroid_pos = asteroid.get_rect(center = (random_x, random_y))
            random_x = random.randint(0, 1280)
            random_y = random.randint(-100, 0)
            new_asteroid.append(asteroid_pos)
 
    keys = pg.key.get_pressed()

    if keys [pg.K_w] and ship_pos.y > 0:  #w to go up (done)
        ship_pos.y -= ship_speed
        window.blit(ship, ship_pos)

    if keys [pg.K_s] and ship_pos.y < 650: #s to go down (done)
        ship_pos.y += ship_speed
        window.blit(ship, ship_pos)

    if keys [pg.K_a] and ship_pos.x > 0:    #a to go left (done)
        ship_pos.x -= ship_speed
        window.blit(ship, ship_pos)

    if keys [pg.K_d] and ship_pos.x < 1215:     #d to go right (done)
        ship_pos.x += ship_speed
        window.blit(ship, ship_pos)

    clock.tick(60)          # maxes game at 60 fps

    window.blit(background, (0,0)) 
    window.blit(ship, ship_pos)
    window.blit(score_text, score_text_pos)
    window.blit(lives_text, lives_text_pos)
    window.blit(level_text, level_text_pos)
    #window.blit(laser, laser_pos)
    window.blit(asteroid, asteroid_pos)
    window.blit(gameOver, gameOver_pos)
    
                
    laser_pos.y -= 10           #laser speed (good)

    for i in new_laser:         #lasers (DONE)
        window.blit(laser, i)
        i.y -= 10
        if i.bottom < 0:
            new_laser.remove(i)
        for j in new_asteroid:
            if i.colliderect(j):    #laser and asteroid collision (FIX lag issue)
                new_laser.remove(i)
                new_asteroid.remove(j)
                score += 1 
                score_text = font1.render('Score: %i' %score, False, 'White') 

    for j in new_asteroid:          #asteroid remover when it passes screen(DONE)
        window.blit(asteroid, j)
        j.y += (2*level)
        if j.bottom > 815:
            new_asteroid.remove(j)

    for k in new_asteroid:              #ship collision (FIX)
        asteroid_pos = k
        if ship_pos.colliderect(asteroid_pos):
            lives -= 1
            lives_text = font1.render('Lives: %i' %lives, False, 'White')
            new_asteroid.remove(k)
    
    if score == 10:          # if score is reached, next level is played (DONE) #CHANGE SCORE HERE
        score = 0   
        level += 1
        spawn_time -= 500
        ship_speed += 1
        level_text = font1.render('Level: %i' %level, False, 'White')
        score_text = font1.render('Score: %i' %score, False, 'White')
        pg.time.set_timer(asteroid_timer, spawn_time)               #asteroid timer
        if spawn_time <= 0:
            pg.time.set_timer(asteroid_timer, 500) 
    
    if lives == 0:
        gameOver_pos = gameOver.get_rect (center = (640, 360))
        pg.time.set_timer(asteroid_timer, 0) 

    pg.display.update() 
