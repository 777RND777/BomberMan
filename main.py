from consts import *
from levels.control import Level


pygame.init()
pygame.display.set_caption("BomberMan")
level = Level()


while not mc.dead:
    if not level.created:
        level.created = True
        level.get_level()
    level.is_finished()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        break
    mc.control(keys)
    mc.is_dead()

    buff_collision()

    level.enemy_movement()

    screen.fill(BG_COLOR)
    level.draw_level()
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
