from consts import *


def draw_level(level):
    draw_edges(level)


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
