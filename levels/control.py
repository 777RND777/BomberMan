from consts import *
import levels.level_1 as l1


class Level:
    def __init__(self):
        self.number = 0
        self.created = False
        self.edges = []
        self.walls = []
        self.enemies = []

    def get_level(self):
        self.number += 1
        self.created = True
        if self.number == 1:
            self.edges = l1.create_edges()
            self.walls = l1.create_walls()
            self.enemies = l1.create_enemies()

    def draw_level(self):
        self.draw_edges()
        self.draw_walls()
        self.draw_enemies()

    def draw_edges(self):
        for i in range(11):
            screen.blit(self.edges[i].image, (0, i * SIZE))
            screen.blit(self.edges[i].image, (WIDTH - SIZE, i * SIZE))
        for i in range(1, 14):
            screen.blit(self.edges[i].image, (i * SIZE, 0))
            screen.blit(self.edges[i].image, (i * SIZE, HEIGHT - SIZE))
        for i in range(1, 7):
            for j in range(1, 5):
                screen.blit(self.edges[i].image, (2 * i * SIZE, 2 * j * SIZE))

    def draw_walls(self):
        wall_group.empty()
        for wall in self.walls:
            wall.is_destroyed()
            if not wall.destroyed:
                wall_group.add(wall)
                screen.blit(wall.image, (wall.rect.x, wall.rect.y))

    def draw_enemies(self):
        enemy_group.empty()
        for enemy in self.enemies:
            enemy.is_dead()
            if not enemy.dead:
                enemy_group.add(enemy)
                screen.blit(enemy.image, (enemy.rect.x, enemy.rect.y))

    def enemy_movement(self):
        for enemy in self.enemies:
            enemy.timer += 1
            enemy.movement()
            if enemy.timer == SIZE:
                enemy.change_direction()
