from consts import *


def draw_level(edges, walls, enemies):
    draw_edges(edges)
    draw_walls(walls)
    draw_enemies(enemies)


def create_edges():
    level = []
    for i in range(11):
        level.append(Edge(SIZE / 2, (i + 0.5) * SIZE))
        level.append(Edge(WIDTH - SIZE / 2, i * SIZE))
    for i in range(1, 14):
        level.append(Edge((i + 0.5) * SIZE, SIZE / 2))
        level.append(Edge(i * SIZE, HEIGHT - SIZE / 2))
    for i in range(1, 7):
        for j in range(1, 5):
            level.append(Edge(2 * i * SIZE + SIZE / 2, 2 * j * SIZE + SIZE / 2))
    return level


def draw_edges(edges):
    for i in range(11):
        screen.blit(edges[i].image, (0, i * SIZE))
        screen.blit(edges[i].image, (WIDTH - SIZE, i * SIZE))
    for i in range(1, 14):
        screen.blit(edges[i].image, (i * SIZE, 0))
        screen.blit(edges[i].image, (i * SIZE, HEIGHT - SIZE))
    for i in range(1, 7):
        for j in range(1, 5):
            screen.blit(edges[i].image, (2 * i * SIZE, 2 * j * SIZE))


def create_walls():
    return [
        Wall(map_scaling(7), map_scaling(3)),
        Wall(map_scaling(11), map_scaling(3)),

        Wall(map_scaling(19), map_scaling(5)),
        Wall(map_scaling(23), map_scaling(5)),
        Wall(map_scaling(27), map_scaling(5)),

        Wall(map_scaling(7), map_scaling(7)),
        Wall(map_scaling(9), map_scaling(7)),
        Wall(map_scaling(19), map_scaling(7)),
        Wall(map_scaling(25), map_scaling(7)),

        Wall(map_scaling(11), map_scaling(9)),

        Wall(map_scaling(5), map_scaling(11)),
        Wall(map_scaling(7), map_scaling(11)),
        Wall(map_scaling(13), map_scaling(11)),
        Wall(map_scaling(15), map_scaling(11)),
        Wall(map_scaling(21), map_scaling(11)),
        Wall(map_scaling(27), map_scaling(11)),
        Wall(map_scaling(27), map_scaling(11)),

        Wall(map_scaling(7), map_scaling(13)),
        Wall(map_scaling(15), map_scaling(13)),
        Wall(map_scaling(23), map_scaling(13)),

        Wall(map_scaling(3), map_scaling(15)),
        Wall(map_scaling(5), map_scaling(15)),
        Wall(map_scaling(9), map_scaling(15)),
        Wall(map_scaling(17), map_scaling(15)),
        Wall(map_scaling(21), map_scaling(15)),
        Wall(map_scaling(23), map_scaling(15)),

        Wall(map_scaling(11), map_scaling(17)),
        Wall(map_scaling(23), map_scaling(17)),

        Wall(map_scaling(9), map_scaling(19)),
        Wall(map_scaling(11), map_scaling(19)),
        Wall(map_scaling(13), map_scaling(19)),
        Wall(map_scaling(15), map_scaling(19)),
        Wall(map_scaling(23), map_scaling(19)),
    ]


def draw_walls(walls):
    wall_group.empty()
    for wall in walls:
        wall.is_destroyed()
        if not wall.destroyed:
            wall_group.add(wall)
            screen.blit(wall.image, (wall.rect.x, wall.rect.y))


def create_enemies():
    return [
        Enemy(map_scaling(17), map_scaling(3)),
        Enemy(map_scaling(13), map_scaling(7)),
        Enemy(map_scaling(23), map_scaling(7)),
        Enemy(map_scaling(9), map_scaling(11)),
        Enemy(map_scaling(19), map_scaling(15)),
    ]


def draw_enemies(enemies):
    enemy_group.empty()
    for enemy in enemies:
        enemy.is_dead()
        if not enemy.dead:
            enemy_group.add(enemy)
            screen.blit(enemy.image, (enemy.rect.x, enemy.rect.y))


def enemy_movement(enemies):
    for enemy in enemies:
        enemy.timer += 1
        enemy.movement()
        if enemy.timer == SIZE:
            enemy.change_direction()
