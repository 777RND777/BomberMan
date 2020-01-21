from consts import *
from levels.level_1 import create_edges, draw_level


pygame.init()
pygame.display.set_caption("BomberMan")
level_edges = create_edges()
mc = MainCharacter(105, 105)
GAME = True

while GAME:
    keys = pygame.key.get_pressed()
    mc.movement(keys)
    if keys[pygame.K_ESCAPE]:
        GAME = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME = False

    screen.fill(BG_COLOR)
    draw_level(level_edges)
    screen.blit(mc.image, mc.rect)

    pygame.display.update()
    pygame.time.delay(DELAY)

    mc.update()
