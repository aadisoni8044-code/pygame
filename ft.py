import pygame

pygame.init()
screen = pygame.display.set_mode((300, 200))
pygame.display.set_caption("LED ON / OFF")

led_on = False
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                led_on = not led_on
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((30, 30, 30))
    color = (0, 255, 0) if led_on else (255, 0, 0)
    pygame.draw.circle(screen, color, (150, 100), 40)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

#  _______|
#         |___on - off___________=switch
#         |_________________________________________| 
#         | pygame switch
          
   




