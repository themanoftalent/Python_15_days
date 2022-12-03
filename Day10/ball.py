#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

import pygame
import random

pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Ball Game")
icon = pygame.image.load('ball.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Ball
ballImg = []
ballX = []
ballY = []
ballX_change = []
ballY_change = []
num_of_balls = 6

for i in range(num_of_balls):
    ballImg.append(pygame.image.load('ball.png'))
    ballX.append(random.randint(0, 735))
    ballY.append(random.randint(50, 150))
    ballX_change.append(4)
    ballY_change.append(40)

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def ball(x, y, i):
    screen.blit(ballImg[i], (x, y))

# Game Loop
running = True
while running:

        # RGB = Red, Green, Blue
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # If keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        # Checking for boundaries of spaceship so it doesn't go out of bounds
        playerX += playerX_change

        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        # Ball Movement
        for i in range(num_of_balls):

            # Game Over
            if ballY[i] > 440:
                for j in range(num_of_balls):
                    ballY[j] = 2000
                game_over_text()
                break

            ballX[i] += ballX_change[i]
            if ballX[i] <= 0:
                ballX_change[i] = 4
                ballY[i] += ballY_change[i]
            elif ballX[i] >= 736:
                ballX_change[i] = -4
                ballY[i] += ballY_change[i]

            # Collision
            collision = isCollision(ballX[i], ballY[i], playerX, playerY)
            if collision:
                ballY[i] = 480
                ballX[i] = random.randint(0, 735)
                score_value += 1

            ball(ballX[i], ballY[i], i)

        player(playerX, playerY)
        show_score(textX, textY)
        pygame.display.update()

# Collision
def isCollision(ballX, ballY, playerX, playerY):
    distance = math.sqrt((math.pow(ballX - playerX, 2)) + (math.pow(ballY - playerY, 2)))
    if distance < 27:
        return True
    else:
        return False

pygame.quit()

