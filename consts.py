from random import randint
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
        self.dead = False
        self.on_bomb = False

    def control(self, keys):
        if keys[pygame.K_RIGHT]:
            self.rect.x += 2
            if is_stop_collision(self):
                self.rect.x -= 2
        if keys[pygame.K_LEFT]:
            self.rect.x -= 2
            if is_stop_collision(self):
                self.rect.x += 2
        if keys[pygame.K_UP]:
            self.rect.y -= 2
            if is_stop_collision(self):
                self.rect.y += 2
        if keys[pygame.K_DOWN]:
            self.rect.y += 2
            if is_stop_collision(self):
                self.rect.y -= 2
        if keys[pygame.K_SPACE]:
            bomb.place()

    def is_dead(self):
        if pygame.sprite.spritecollideany(self, boom_group) or pygame.sprite.spritecollideany(self, enemy_group):
            self.dead = True


class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, bomb_group)
        self.image = pygame.transform.scale(pygame.image.load("img/bomb.png").convert_alpha(), HERO_XY)
        self.rect = self.image.get_rect(center=(x, y))
        self.is_placed = False
        self.timer = 300
        self.size = 1

    def place(self):
        if not self.is_placed:
            self.is_placed = True
            mc.on_bomb = True
            self.rect.x = mc.rect.x
            self.rect.y = mc.rect.y
            self.fix_place()

    def fix_place(self):
        for i in range(SIZE, WIDTH - 2 * SIZE, SIZE):
            if self.rect.x in range(i - int(HERO_SIZE / 2), i + SIZE - int(HERO_SIZE / 2)):
                self.rect.x = i + 10
                break
        for i in range(SIZE, WIDTH - 2 * SIZE, SIZE):
            if self.rect.y in range(i - int(HERO_SIZE / 2), i + SIZE - int(HERO_SIZE / 2)):
                self.rect.y = i + 10
                break

    def timer_action(self):
        self.timer -= 1
        if self.timer == 200:
            self.almost_explode()
        if self.timer == 100:
            self.explode()
        if self.timer == 0:
            self.hide()

    def almost_explode(self):
        self.image = pygame.transform.scale(pygame.image.load("img/red_bomb.png").convert_alpha(), HERO_XY)

    def explode(self):
        horizontal_boom.rect.x = self.rect.x - self.size * SIZE - 10
        horizontal_boom.rect.y = self.rect.y
        vertical_boom.rect.x = self.rect.x
        vertical_boom.rect.y = self.rect.y - self.size * SIZE - 10

    def hide(self):
        self.is_placed = False
        self.timer = 300
        self.image = pygame.transform.scale(pygame.image.load("img/bomb.png").convert_alpha(), HERO_XY)
        hide(bomb)
        hide(horizontal_boom)
        hide(vertical_boom)


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self, boom_group)
        self.image = pygame.transform.scale(pygame.image.load("img/blow.png").convert_alpha(), size)
        self.rect = self.image.get_rect(center=(x, y))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, enemy_group)
        self.image = pygame.transform.scale(pygame.image.load("img/enemy.png").convert_alpha(), XY)
        self.rect = self.image.get_rect(center=(x, y))
        self.dead = False
        self.direction = 1
        self.timer = 0
        self.on_bomb = False

    def is_dead(self):
        if pygame.sprite.spritecollideany(self, boom_group):
            self.dead = True

    def movement(self):
        if self.direction == 1:
            self.rect.y -= 2
            if is_stop_collision(self):
                self.rect.y += 2
                self.change_direction()
        if self.direction == 2:
            self.rect.x += 2
            if is_stop_collision(self):
                self.rect.x -= 2
                self.change_direction()
        if self.direction == 3:
            self.rect.y += 2
            if is_stop_collision(self):
                self.rect.y -= 2
                self.change_direction()
        if self.direction == 4:
            self.rect.x -= 2
            if is_stop_collision(self):
                self.rect.x += 2
                self.change_direction()

    def change_direction(self):
        self.direction = randint(1, 4)
        self.timer = 0


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("img/wall.png").convert_alpha(), XY)
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


def map_scaling(num):
    return num * SIZE / 2


def is_stop_collision(sprite):
    if pygame.sprite.spritecollideany(sprite, edge_group):
        return True
    if pygame.sprite.spritecollideany(sprite, wall_group):
        return True
    if pygame.sprite.spritecollideany(sprite, bomb_group):
        if not sprite.on_bomb:
            return True
    else:
        sprite.on_bomb = False
    return False


def hide(sprite):
    sprite.rect.x = 0
    sprite.rect.y = 0


# pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bomb_group = pygame.sprite.Group()
boom_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
edge_group = pygame.sprite.Group()

mc = MainCharacter(105, 105)
bomb = Bomb(0, 0)
horizontal_boom = Explosion(0, 0, ((2 * bomb.size + 1) * SIZE, HERO_SIZE))
vertical_boom = Explosion(0, 0, (HERO_SIZE, (2 * bomb.size + 1) * SIZE))
