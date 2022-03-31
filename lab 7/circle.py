import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("CIRCLE")

finished = False

x, y = 400, 300
clock = pygame.time.Clock()

while not finished:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y - 25 > 0:
        y += -20
    if keys[pygame.K_DOWN] and y + 25 < 600:
        y += 20
    if keys[pygame.K_LEFT] and x - 25 > 0:
        x += -20
    if keys[pygame.K_RIGHT] and x + 25 < 800:
        x += 20
        
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
    
    pygame.display.flip()
pygame.quit()