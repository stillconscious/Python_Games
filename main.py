import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800, 400))

pygame.display.set_caption('Snake Game')
Clock = pygame.time.Clock()
game_back = pygame.image.load('C:\\Users\\A n s h u\\OneDrive\\Pictures\\snake_background.png').convert()
snake = pygame.image.load('C:\\Users\\A n s h u\\OneDrive\\Pictures\\snake.png').convert_alpha()
snake_rect = snake.get_rect(midleft=(400, 200))
heart = pygame.image.load('C:\\Users\\A n s h u\\OneDrive\\Pictures\\heart.png').convert()
heart_rect = heart.get_rect(midleft=(600, 300))
x_change = 0
y_change = 0
obstacle1 = pygame.image.load('C:\\Users\\A n s h u\\OneDrive\\Pictures\\obstacle.png').convert()
obstacle_rect1 = obstacle1.get_rect(midleft=(300, 100))
obstacle2 = pygame.image.load('C:\\Users\\A n s h u\\OneDrive\\Pictures\\obstacle.png').convert()
obstacle_rect2 = obstacle2.get_rect(midleft=(300, 300))
obstacle_vert1 = pygame.image.load('C:\\Users\\A n s h u\\OneDrive\\Pictures\\obstacle_vert.png').convert()
obstaclevert_rect1 = obstacle_vert1.get_rect(midleft=(200, 100))
obstacle_vert2 = pygame.image.load('C:\\Users\\A n s h u\\OneDrive\\Pictures\\obstacle_vert.png').convert()
obstaclevert_rect2 = obstacle_vert2.get_rect(midleft=(200, 300))
obstacle_vert3 = pygame.image.load('C:\\Users\\A n s h u\\OneDrive\\Pictures\\obstacle_vert.png').convert()
obstaclevert_rect3 = obstacle_vert3.get_rect(midleft=(600, 100))
obstacle_vert4 = pygame.image.load('C:\\Users\\A n s h u\\OneDrive\\Pictures\\obstacle_vert.png').convert()
obstaclevert_rect4 = obstacle_vert4.get_rect(midleft=(600, 300))
info = pygame.font.Font(None, 40)
score = 0
lastmessage = pygame.font.Font(None, 40)
yes = lastmessage.render("YES", False, (0, 0, 0))
yes_surface = yes.get_rect(midleft=(200, 240))
no = lastmessage.render("NO", False, (0, 0, 0))
no_surface = no.get_rect(midleft=(500, 240))
speed_increase = 3


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(game_back, (0, 0))
    screen.blit(obstacle1, obstacle_rect1)
    screen.blit(obstacle2, obstacle_rect2)
    screen.blit(obstacle_vert1, obstaclevert_rect1)
    screen.blit(obstacle_vert2, obstaclevert_rect2)
    screen.blit(obstacle_vert3, obstaclevert_rect3)
    screen.blit(obstacle_vert4, obstaclevert_rect4)
    screen.blit(snake, snake_rect)
    snake_rect.y += y_change
    snake_rect.x += x_change
    if snake_rect.midleft[0] >= 800:
        snake_rect.x = 0
    elif snake_rect.midright[0] <= 0:
        snake_rect.x = 800
    elif snake_rect.midtop[1] >= 400:
        snake_rect.y = 0
    elif snake_rect.midbottom[1] <= 1:
        snake_rect.y = 400
    while snake_rect.colliderect(heart_rect):
        heart_rect.x = random.randrange(4, 790)
        heart_rect.y = random.randrange(0, 400)
        score = score + 1
    while heart_rect.colliderect(obstacle_rect1) or heart_rect.colliderect(obstacle_rect2) or heart_rect.colliderect(obstaclevert_rect1) or heart_rect.colliderect(obstaclevert_rect2) or heart_rect.colliderect(obstaclevert_rect3) or heart_rect.colliderect(obstaclevert_rect4):
        heart_rect.x = random.randrange(4, 790)
        heart_rect.y = random.randrange(20, 380)
    screen.blit(heart, heart_rect)
    keys = pygame.key.get_pressed()
    speed_increase = 3
    if snake_rect.colliderect(heart_rect):
        score += 1
        speed_increase += 10

    infosur = info.render(str(score), False, (0, 230, 200))
    screen.blit(infosur, (765, 0))
    if keys[pygame.K_LEFT]:
        x_change = -speed_increase
        y_change = 0
    elif keys[pygame.K_RIGHT]:
        x_change = speed_increase
        y_change = 0
    elif keys[pygame.K_UP]:
        y_change = -speed_increase
        x_change = 0
    elif keys[pygame.K_DOWN]:
        y_change = speed_increase
        x_change = 0
    lastm = lastmessage.render("SCORE = " + str(score) + "   ,Do you want to play again?", False,
                               (0, 0, 0))
    if snake_rect.colliderect(obstacle_rect1) or snake_rect.colliderect(obstacle_rect2) or snake_rect.colliderect(
            obstaclevert_rect1) or snake_rect.colliderect(obstaclevert_rect2) or snake_rect.colliderect(
            obstaclevert_rect3) or snake_rect.colliderect(obstaclevert_rect4):

        x_change = 0
        y_change = 0
        screen.blit(lastm, (150, 100))
        pygame.draw.rect(screen, 'pink', yes_surface)
        pygame.draw.rect(screen, 'pink', no_surface)
        screen.blit(yes, yes_surface)
        screen.blit(no, no_surface)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if yes_surface.collidepoint(pygame.mouse.get_pos()):
                    snake_rect.x = 400
                    snake_rect.y = 200
                    score = 0
                elif no_surface.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    exit()
                else:
                    pass


    pygame.display.update()
    Clock.tick(60)


