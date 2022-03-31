import pygame
import datetime

pygame.init()

secund = -(int(datetime.datetime.now().strftime("%S")) * 6) - 6
minut = -(int(datetime.datetime.now().strftime("%M")) * 6 + (int(datetime.datetime.now().strftime("%M")) * 6 / 60)) - 54
background = pygame.image.load('./images/mickeyclock12.png')
second = pygame.image.load('./images/test.png')
minute = pygame.image.load('./images/minut.png')

def rotate(image, rect, angle):
    new_image = pygame.transform.rotate(image, angle)
    rect = new_image.get_rect(center=rect.center)
    return new_image, rect


#ruki
image = pygame.Surface((63, 1050), pygame.SRCALPHA)
image.blit(second, (0, 0))  
orig_image = image
rect = image.get_rect(center=(1400//2, 1050//2))

imagem = pygame.Surface((1400, 1050), pygame.SRCALPHA)
imagem.blit(minute, (0, 0))
orig_imagem = imagem
rect1 = imagem.get_rect(center=(1400//2, 1050//2))
#-----------------------------------------------------
screen = pygame.display.set_mode((1400, 1050))
pygame.display.set_caption("Mickey Clock")

done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(60)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
     
    screen.blit(background, (0, 0)) 
    screen.blit(image, rect)
    screen.blit(imagem, rect1)
    image, rect = rotate(orig_image, rect, secund)
    imagem, rect1 = rotate(orig_imagem, rect1, minut)

    secund -= 0.099
    minut = minut - (0.099 / 60)
    
    pygame.display.flip()

pygame.quit()
    

