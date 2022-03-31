import os
import pygame

pygame.init()

screen = pygame.display.set_mode((200, 200))
player = True
done = False
path = ''
pygame.mixer.music.load('./music/hello.mp3')
while player:
    pygame.mixer.music.play(1)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player = not player
                done = not done
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                path = input()
                _ = pygame.mixer.Sound(f'./music/{path}.mp3')
                _.play(1)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_o:
                pygame.mixer.pause()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                pygame.mixer.unpause()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                pygame.mixer.pause()
                path = int(path) + 1
                _ = pygame.mixer.Sound(f'./music/{path}.mp3')
                _.play(1)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.mixer.pause()
                path = int(path) - 1
                _ = pygame.mixer.Sound(f'./music/{path}.mp3')
                _.play(1)         
pygame.quit()