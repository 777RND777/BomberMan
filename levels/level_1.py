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


def draw_edges(level):
    for i in range(11):
        screen.blit(level[i].image, (0, i * SIZE))
        screen.blit(level[i].image, (WIDTH - SIZE, i * SIZE))
    for i in range(1, 14):
        screen.blit(level[i].image, (i * SIZE, 0))
        screen.blit(level[i].image, (i * SIZE, HEIGHT - SIZE))
    for i in range(1, 7):
        for j in range(1, 5):
            screen.blit(level[i].image, (2 * i * SIZE, 2 * j * SIZE))


def create_walls():
    return [
        Wall(7 * SIZE / 2, 3 * SIZE / 2),
        Wall(11 * SIZE / 2, 3 * SIZE / 2),

        Wall(19 * SIZE / 2, 5 * SIZE / 2),
        Wall(23 * SIZE / 2, 5 * SIZE / 2),
        Wall(27 * SIZE / 2, 5 * SIZE / 2),

        Wall(7 * SIZE / 2, 7 * SIZE / 2),
        Wall(9 * SIZE / 2, 7 * SIZE / 2),
        Wall(19 * SIZE / 2, 7 * SIZE / 2),
        Wall(25 * SIZE / 2, 7 * SIZE / 2),

        Wall(11 * SIZE / 2, 9 * SIZE / 2),

        Wall(5 * SIZE / 2, 11 * SIZE / 2),
        Wall(7 * SIZE / 2, 11 * SIZE / 2),
        Wall(13 * SIZE / 2, 11 * SIZE / 2),
        Wall(15 * SIZE / 2, 11 * SIZE / 2),
        Wall(21 * SIZE / 2, 11 * SIZE / 2),
        Wall(27 * SIZE / 2, 11 * SIZE / 2),

        Wall(7 * SIZE / 2, 13 * SIZE / 2),
        Wall(15 * SIZE / 2, 13 * SIZE / 2),
        Wall(19 * SIZE / 2, 13 * SIZE / 2),
        Wall(23 * SIZE / 2, 13 * SIZE / 2),
        Wall(27 * SIZE / 2, 13 * SIZE / 2),

        Wall(3 * SIZE / 2, 15 * SIZE / 2),
        Wall(5 * SIZE / 2, 15 * SIZE / 2),
        Wall(9 * SIZE / 2, 15 * SIZE / 2),
        Wall(17 * SIZE / 2, 15 * SIZE / 2),

        Wall(11 * SIZE / 2, 17 * SIZE / 2),
        Wall(23 * SIZE / 2, 17 * SIZE / 2),

        Wall(9 * SIZE / 2, 19 * SIZE / 2),
        Wall(11 * SIZE / 2, 19 * SIZE / 2),
        Wall(13 * SIZE / 2, 19 * SIZE / 2),
        Wall(15 * SIZE / 2, 19 * SIZE / 2),
        Wall(25 * SIZE / 2, 19 * SIZE / 2),
    ]


def draw_walls(level):
    wall_group.empty()
    for wall in level:
        wall.is_destroyed()
        if not wall.destroyed:
            wall_group.add(wall)
            screen.blit(wall.image, (wall.rect.x, wall.rect.y))


def create_enemies():
    return [
        Enemy(275, 120),
    ]


def draw_enemies(level):
    enemy_group.empty()
    for enemy in level:
        enemy.is_dead()
        if not enemy.dead:
            enemy_group.add(enemy)
            screen.blit(enemy.image, (enemy.rect.x, enemy.rect.y))
