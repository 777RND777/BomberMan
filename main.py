import pygame


pygame.init()
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Bomberman")
hero_size = (50, 50)
size = (90, 90)
delay = 8
game = True
bg_color = (0, 149, 0)
bomb_placed = False


class MainCharacter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("img/mc.png").convert_alpha(), hero_size)
        self.rect = self.image.get_rect(center=(x, y))

    def movement(self):
        if keys[pygame.K_RIGHT]:
            self.rect.x += 2
        if keys[pygame.K_LEFT]:
            self.rect.x -= 2
        if keys[pygame.K_UP]:
            self.rect.y -= 2
        if keys[pygame.K_DOWN]:
            self.rect.y += 2
        if keys[pygame.K_SPACE]:
            if not bomb.placed:
                bomb.placed = True
                bomb.rect.x = mc.rect.x
                bomb.rect.y = mc.rect.y


class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("img/bomb1.png").convert_alpha(), size)
        self.rect = self.image.get_rect(center=(x, y))
        self.placed = False


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("img/wall.jpg").convert_alpha(), size)
        self.rect = self.image.get_rect(center=(x, y))


class Edge(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("img/edge.png").convert_alpha(), size)
        self.rect = self.image.get_rect(center=(x, y))


mc = MainCharacter(0, 0)
bomb = Bomb(0, 0)
wall1 = Wall(0, 0)
edge = Edge(0, 0)


while game:
    keys = pygame.key.get_pressed()
    mc.movement()
    if keys[pygame.K_ESCAPE]:
        game = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    screen.fill(bg_color)
    screen.blit(edge.image, (100, 100))
    screen.blit(edge.image, (200, 100))
    screen.blit(mc.image, mc.rect)
    if bomb_placed:
        screen.blit(bomb.image, bomb.rect)
    screen.blit(wall1.image, wall1.rect)
    pygame.display.update()
    pygame.time.delay(delay)

    mc.update()
    wall1.update()
