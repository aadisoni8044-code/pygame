import pygame
import webbrowser
import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("aadi soni ")

# Colors
WHITE = (255, 255, 255)
GREEN = (37, 211, 102)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont(None, 40)

# Button
button_rect = pygame.Rect(150, 120, 200, 60)

running = True
while running:
    screen.fill(WHITE)

    # Button
    pygame.draw.rect(screen, GREEN, button_rect, border_radius=10)
    text = font.render("aadi soni", True, BLACK)
    screen.blit(text, (button_rect.x + 25, button_rect.y + 15))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                webbrowser.open("Github.com/aadisoni8044-code")

    pygame.display.update()

pygame.quit()

sys.exit()



#____________________pygame -------------
