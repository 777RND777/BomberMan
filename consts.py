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

# pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bomb_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
edge_group = pygame.sprite.Group()


# classes
class MainCharacter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("img/mc.png").convert_alpha(), HERO_XY)
        self.rect = self.image.get_rect(center=(x, y))

    def movement(self, keys):
        if keys[pygame.K_RIGHT]:
            self.rect.x += 2
            if pygame.sprite.spritecollideany(self, edge_group):
                self.rect.x -= 2
        if keys[pygame.K_LEFT]:
            self.rect.x -= 2
            if pygame.sprite.spritecollideany(self, edge_group):
                self.rect.x += 2
        if keys[pygame.K_UP]:
            self.rect.y -= 2
            if pygame.sprite.spritecollideany(self, edge_group):
                self.rect.y += 2
        if keys[pygame.K_DOWN]:
            self.rect.y += 2
            if pygame.sprite.spritecollideany(self, edge_group):
                self.rect.y -= 2


class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, bomb_group)
        self.image = pygame.transform.scale(pygame.image.load("img/bomb1.png").convert_alpha(), HERO_XY)
        self.rect = self.image.get_rect(center=(x, y))
        self.placed = False

    def explode(self):
        self.image = pygame.transform.scale(pygame.image.load("img/blow.png").convert_alpha(), HERO_XY)


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, wall_group)
        self.image = pygame.transform.scale(pygame.image.load("img/wall.jpg").convert_alpha(), XY)
        self.rect = self.image.get_rect(center=(x, y))
        self.destroyed = False


class Edge(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, edge_group)
        self.image = pygame.transform.scale(pygame.image.load("img/edge.png").convert_alpha(), XY)
        self.rect = self.image.get_rect(center=(x, y))
