from consts import *
from random import randint
import levels.level_1 as l1
import levels.level_2 as l2


class Level:
    def __init__(self):
        self.number = 0
        self.created = False
        self.bomb_buffs = []
        self.door = Door()
        self.edges = []
        self.walls = []
        self.enemies = []

    def create_level(self):
        self.created = True
        self.get_level()
        self.hide_behind_wall(self.door)
        for buff in self.bomb_buffs:
            self.hide_behind_wall(buff)

    def get_level(self):
        self.number += 1
        self.created = True
        if self.number == 1:
            self.bomb_buffs = l1.bomb_buffs
            self.enemies = l1.enemies
            self.walls = l1.walls
            self.edges = l1.create_edges()
        if self.number == 2:
            self.bomb_buffs = l2.bomb_bonus
            self.enemies = l2.enemies
            self.walls = l2.walls

    def draw_level(self):
        self.draw_bomb_buffs()
        screen.blit(self.door.image, (self.door.rect.x, self.door.rect.y))
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

    def hide_behind_wall(self, sprite):
        # TODO remove this check later
        if len(self.walls) > 0:
            while True:
                i = randint(0, len(self.walls) - 1)
                if not self.walls[i].hide_object:
                    sprite.rect = self.walls[i].rect
                    self.walls[i].hide_object = True
                    break

    def is_finished(self):
        if pygame.sprite.spritecollideany(self.door, mc_group):
            self.created = False
            mc.rect.x = map_scaling(3) - 20
            mc.rect.y = map_scaling(3) - 20
