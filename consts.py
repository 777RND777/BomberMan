import pygame


# sizes
WIDTH, HEIGHT = 1050, 770
HERO_SIZE = 50
HERO_XY = (HERO_SIZE, HERO_SIZE)
SIZE = 70
XY = (SIZE, SIZE)

# gameplay
BG_COLOR = (0, 149, 0)
DELAY = 5


# classes
class MainCharacter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("img/mc.png").convert_alpha(), HERO_XY)
        self.rect = self.image.get_rect(center=(x, y))

    def control(self, keys):
        if keys[pygame.K_RIGHT]:
            self.rect.x += 2
            if pygame.sprite.spritecollideany(self, edge_group) or pygame.sprite.spritecollideany(self, wall_group):
                self.rect.x -= 2
        if keys[pygame.K_LEFT]:
            self.rect.x -= 2
            if pygame.sprite.spritecollideany(self, edge_group) or pygame.sprite.spritecollideany(self, wall_group):
                self.rect.x += 2
        if keys[pygame.K_UP]:
            self.rect.y -= 2
            if pygame.sprite.spritecollideany(self, edge_group) or pygame.sprite.spritecollideany(self, wall_group):
                self.rect.y += 2
        if keys[pygame.K_DOWN]:
            self.rect.y += 2
            if pygame.sprite.spritecollideany(self, edge_group) or pygame.sprite.spritecollideany(self, wall_group):
                self.rect.y -= 2
        if keys[pygame.K_SPACE]:
            if not bomb.placed:
                bomb.placed = True
                bomb.rect.x = self.rect.x
                bomb.rect.y = self.rect.y


class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, bomb_group)
        self.image = pygame.transform.scale(pygame.image.load("img/bomb.png").convert_alpha(), HERO_XY)
        self.rect = self.image.get_rect(center=(x, y))
        self.placed = False
        self.explosion = False
        self.timer = 0
        self.size = 1

    def explode(self):
        self.image = pygame.transform.scale(pygame.image.load("img/blow.png").convert_alpha(), HERO_XY)
        self.explosion = True
        horizontal_boom.rect.x = self.rect.x - 70
        horizontal_boom.rect.y = self.rect.y
        vertical_boom.rect.x = self.rect.x
        vertical_boom.rect.y = self.rect.y - 70

    def hide(self):
        self.placed = False
        self.explosion = False
        self.timer = 0
        self.image = pygame.transform.scale(pygame.image.load("img/bomb.png").convert_alpha(), HERO_XY)


class VerticalExplosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, boom_group)
        self.image = pygame.transform.scale(pygame.image.load("img/blow.png").convert_alpha(),
                                            (SIZE, (2 * bomb.size + 1) * SIZE))
        self.rect = self.image.get_rect(center=(x, y))


class HorizontalExplosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, boom_group)
        self.image = pygame.transform.scale(pygame.image.load("img/blow.png").convert_alpha(),
                                            ((2 * bomb.size + 1) * SIZE, SIZE))
        self.rect = self.image.get_rect(center=(x, y))


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("img/wall.jpg").convert_alpha(), XY)
        self.rect = self.image.get_rect(center=(x, y))
        self.destroyed = False

    def is_destroyed(self):
        if pygame.sprite.spritecollideany(self, boom_group):
            self.destroyed = True


class Edge(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, edge_group)
        self.image = pygame.transform.scale(pygame.image.load("img/edge.png").convert_alpha(), XY)
        self.rect = self.image.get_rect(center=(x, y))


# pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bomb_group = pygame.sprite.Group()
boom_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
edge_group = pygame.sprite.Group()

mc = MainCharacter(105, 105)
bomb = Bomb(0, 0)
vertical_boom = VerticalExplosion(0, 0)
horizontal_boom = HorizontalExplosion(0, 0)
