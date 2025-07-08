import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bosganda Ishlaydigan O‘yin")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_pos = [400, 300]
ball_radius = 30
ball_speed = [4, 4]
moving = False  # To‘p harakatlanyaptimi yoki yo‘q

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(100)
    window.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True

        # Foydalanuvchi sichqoncha bosganini tekshirish
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            # To‘pga tegildimi (masofa bo‘yicha)
            distance = math.sqrt((mouse_x - ball_pos[0])**2 + (mouse_y - ball_pos[1])**2)
            if distance <= ball_radius:
                moving = True

    # Agar bosilgan bo‘lsa to‘p harakatlanadi
    if moving:
        ball_pos[0] += ball_speed[0]
        ball_pos[1] += ball_speed[1]

        # Chegaralarga tegsa orqaga qaytarish
        if ball_pos[0] - ball_radius <= 0 or ball_pos[0] + ball_radius >= WIDTH:
            ball_speed[0] *= -1
        if ball_pos[1] - ball_radius <= 0 or ball_pos[1] + ball_radius >= HEIGHT:
            ball_speed[1] *= -1

    pygame.draw.circle(window, RED, ball_pos, ball_radius)
    pygame.display.update()

pygame.quit()
sys.exit()
