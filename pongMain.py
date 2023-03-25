'''
Luis Garcia
Pong in Python 3
3/22/2023

This uses pygame to recreate the classic arcade game Pong
The Paddles, Ball, and Score modules import pygame in the files where their defintions are
They were designed for use in this project, the nice thing is that pygame is quite popular
'''

import pygame
import Paddles
import Ball
import Score

#Define screen size
ds_width = 1280
ds_height = 720

#Pygame setup
pygame.init()
ds = pygame.display.set_mode((ds_width, ds_height))
clock = pygame.time.Clock()

#Player paddle & score
player1 = Paddles.paddle("white", 20, 20, 20, 100) #paddle(color, x-coord, y-coord, width, height)
p1_score = Score.score()

#Computer paddle & score
player2 = Paddles.paddle("white", ds_width - 40, 20, 20, 100)
p2_score = Score.score()

#Ball
pingPong = Ball.ball("pink", ds_width/2, ds_height/2, 10)

def render(ds):
    player1.draw(ds)
    player2.draw(ds)
    pingPong.draw(ds)

    #These are displayed differently because of how pygame handles rendering text
    #Paddles are pygame rect objects which have a draw method
    #pygame takes text and generates a surface which I have to blit to the game window
    p1ScrSurf, _ = p1_score.renderScore()
    p2ScrSurf, _ = p2_score.renderScore()

    ds.blit(p1ScrSurf, (ds_width/4, 20))
    ds.blit(p2ScrSurf, (3*(ds_width/4), 20))

def enforceBounds(p1, p2, pingPong):
    #If player goes above the screen
    if (p1.ypos < 0):
        p1.setPos(0) #Set the player's y-coord to zero
    
    if (p2.ypos < 0):
        p2.setPos(0) #Set the player's y-coord to zero

    #If player's bottom edge goes below the screen
    if ((p1.ypos + p1.h) > ds_height):
        p1.setPos(ds_height - p1.h)

    if ((p2.ypos + p2.h) > ds_height):
        p2.setPos(ds_height - p2.h)

    #If the pingPong hits the top or bottom of the screen, bounce
    if (pingPong.ypos - pingPong.radius < 0) or (pingPong.ypos + pingPong.radius > ds_height):
        pingPong.dY *= -1

    #If the pingPong hits the left or right edge of the screen, rest, ball and increment score
    if (pingPong.xpos - pingPong.radius < 0):
        pingPong.resetBall(ds_width, ds_height)
        #If the ball goes past the p1 paddle, then p2 earns the point
        p2_score.incrementScore()
        
    if (pingPong.xpos + pingPong.radius > ds_width):
        pingPong.resetBall(ds_width, ds_height)
        p1_score.incrementScore()
        
def main():
    run = True
    p1_yVel = 0
    p2_yVel = 0

    #Game loop
    while run:
        #max FPS is 60, tDelta is the time from the last call to tick() and current call
        tDelta = clock.tick(60)
        
        for event in pygame.event.get():

            #Check if the quit button is pressed
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                #Y coordinate is reversed in computer graphics (Origin is top left)
                #When the player presses up key, move up
                if event.key == pygame.K_UP:
                    p1_yVel = -300 #Idk what units these are since we use a time delta later too
                #When the player presses down key, move down
                if event.key == pygame.K_DOWN:
                    p1_yVel = 300
                    
            if event.type == pygame.KEYUP:
                #When the player releases the up or down key set velocity to zero
                if event.key == pygame.K_UP or pygame.K_DOWN:
                    p1_yVel = 0

        #Covers anything left behind from last frame
        ds.fill("black")

        #Render the game here
        #=========================
        tDelta /= 1000 #Convert milliseconds to seconds
        
        player1.move(p1_yVel * tDelta)

        #The "ai" simply checks if the pingPong is above the top edge of the paddle or below the bottom edge
        #and sets the velocity to upwards or downwards
        p2_yVel = player2.ai_move( pingPong )

        #This actually moves the paddle on the screen
        player2.move(p2_yVel * tDelta)

        #The pingPong's angle angle and speed come from a random yVel -500 to 500, w/ a fixed xVel = +/- 300
        pingPong.move( tDelta )
        #Check whether the pingPong collides with either paddle, if so then reverse xVel
        pingPong.checkBounce(player1, player2)

        #If the pingPong hits the top or bottom edge of the screen, reverse yVel
        enforceBounds(player1, player2, pingPong)
        
        render(ds)
        
        #update display
        pygame.display.flip()
        
main()
pygame.quit()
