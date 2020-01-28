from consts import *
import levels.level_1 as l1


class Level:
    def __init__(self):
        self.number = 0
        self.created = False
        self.edges = []
        self.walls = []
        self.enemies = []
        self.bomb_buffs = []

    def get_level(self):
        self.number += 1
        self.created = True
        if self.number == 1:
            self.bomb_buffs = l1.create_bomb_buffs()
            self.enemies = l1.create_enemies()
            self.walls = l1.create_walls()
            self.edges = l1.create_edges()

    def draw_level(self):
        self.draw_bomb_buffs()
        self.draw_enemies()
        self.draw_walls()
        self.draw_edges()

    def draw_bomb_buffs(self):
        bomb_buff_group.empty()
        for buff in self.bomb_buffs:
            if not buff.is_picked:
                bomb_buff_group.add(buff)
                screen.blit(buff.image, (buff.rect.x, buff.rect.y))

    def draw_enemies(self):
        enemy_group.empty()
        for enemy in self.enemies:
            enemy.is_dead()
            if not enemy.dead:
                enemy_group.add(enemy)
                screen.blit(enemy.image, (enemy.rect.x, enemy.rect.y))

    def draw_walls(self):
        wall_group.empty()
        for wall in self.walls:
            wall.is_destroyed()
            if not wall.destroyed:
                wall_group.add(wall)
                screen.blit(wall.image, (wall.rect.x, wall.rect.y))

    def draw_edges(self):
        for edge in self.edges:
            screen.blit(edge.image, edge.rect)

    def enemy_movement(self):
        for enemy in self.enemies:
            enemy.timer += 1
            enemy.movement()
            if enemy.timer == SIZE:
                enemy.change_direction()
