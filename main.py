from consts import *
import levels.level_1 as l1


pygame.init()
pygame.display.set_caption("BomberMan")
level_edges = l1.create_edges()
level_walls = l1.create_walls()
level_enemies = l1.create_enemies()


while not mc.dead:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        break
    mc.control(keys)

    screen.fill(BG_COLOR)
    l1.draw_level(level_edges, level_walls, level_enemies)
    if bomb.is_placed:
        screen.blit(bomb.image, bomb.rect)
        bomb.timer_action()
        if bomb.timer < 100:
            screen.blit(vertical_boom.image, vertical_boom.rect)
            screen.blit(horizontal_boom.image, horizontal_boom.rect)
    screen.blit(mc.image, mc.rect)

    pygame.display.update()
    pygame.time.delay(DELAY)

    mc.update()
