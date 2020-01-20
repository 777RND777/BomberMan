from consts import *
from threading import Timer
import pygame


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BomberMan")
GAME = True

bomb_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
edge_group = pygame.sprite.Group()


class MainCharacter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("img/mc.png").convert_alpha(), HERO_XY)
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


mc = MainCharacter(105, 105)
bomb = Bomb(0, 0)
wall = Wall(0, 0)
edge = Edge(0, 0)


def edges():
    for i in range(10):
        screen.blit(edge.image, (0, i * SIZE))
    for i in range(10):
        screen.blit(edge.image, (WIDTH - SIZE, i * SIZE))
    for i in range(15):
        screen.blit(edge.image, (i * SIZE, 0))
    for i in range(15):
        screen.blit(edge.image, (i * SIZE, HEIGHT - SIZE))
    for i in range(1, 7):
        for j in range(1, 5):
            screen.blit(edge.image, (2 * i * SIZE, 2 * j * SIZE))


def walls():
    screen.blit(wall.image, (70, 210))
    screen.blit(wall.image, (210, 140))
    screen.blit(wall.image, (280, 70))


while GAME:
    keys = pygame.key.get_pressed()
    mc.movement()
    if pygame.sprite.spritecollideany(mc, edge_group):
        GAME = False
    if keys[pygame.K_ESCAPE]:
        GAME = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME = False

    screen.fill(BG_COLOR)
    edges()
    walls()
    screen.blit(mc.image, mc.rect)
    if bomb.placed:
        screen.blit(bomb.image, bomb.rect)
    pygame.display.update()
    pygame.time.delay(DELAY)

    mc.update()
    wall.update()
