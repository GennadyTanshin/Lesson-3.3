import pygame
import random
pygame.init()
score = 0
sub=0

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption(f"Игра Тир. Счёт {score}")
icon= pygame.image.load("img/photo.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width=50
target_height=50

target_x= random.randint(0,SCREEN_WIDTH-target_width)
target_y= random.randint(0,SCREEN_HEIGHT-target_height)

color =(random.randint(0,255), random.randint(0,255), random.randint(0,255))


running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1
                sub+=2
                pygame.display.set_caption(f"Игра Тир. Счёт {score}. Уменьшение разера мишени на {sub} пикселей")
                target_width = max(10, target_width - 2)
                target_height = max(10, target_height - 2)
                target_img = pygame.transform.scale(target_img, (target_width, target_height))
                if target_width == 10:
                    pygame.display.set_caption(f"Игра Тир. Счёт {score},  Молодец! Хорошая точность. Ты выиграл.")
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    screen.blit(target_img,(target_x, target_y))
    pygame.display.update()





pygame.quit()