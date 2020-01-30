from consts import *


bomb_bonus = [BombBonus()]
enemies = [
    Enemy(map_scaling(11), map_scaling(3)),
    Enemy(map_scaling(19), map_scaling(11)),
    Enemy(map_scaling(9), map_scaling(15)),
    Enemy(map_scaling(27), map_scaling(17)),
    Enemy(map_scaling(7), map_scaling(19)),
    Enemy(map_scaling(15), map_scaling(19)),
]
walls = [
    Wall(map_scaling(7), map_scaling(3)),
    Wall(map_scaling(19), map_scaling(3)),

    Wall(map_scaling(7), map_scaling(5)),
    Wall(map_scaling(11), map_scaling(5)),
    Wall(map_scaling(27), map_scaling(5)),

    Wall(map_scaling(3), map_scaling(7)),
    Wall(map_scaling(13), map_scaling(7)),
    Wall(map_scaling(15), map_scaling(7)),
    Wall(map_scaling(21), map_scaling(7)),
    Wall(map_scaling(23), map_scaling(7)),

    Wall(map_scaling(7), map_scaling(9)),
    Wall(map_scaling(15), map_scaling(9)),
    Wall(map_scaling(27), map_scaling(9)),

    Wall(map_scaling(3), map_scaling(11)),
    Wall(map_scaling(9), map_scaling(11)),
    Wall(map_scaling(11), map_scaling(11)),
    Wall(map_scaling(15), map_scaling(11)),
    Wall(map_scaling(27), map_scaling(11)),

    Wall(map_scaling(3), map_scaling(13)),
    Wall(map_scaling(15), map_scaling(13)),

    Wall(map_scaling(5), map_scaling(15)),
    Wall(map_scaling(11), map_scaling(15)),
    Wall(map_scaling(19), map_scaling(15)),
    Wall(map_scaling(23), map_scaling(15)),

    Wall(map_scaling(7), map_scaling(17)),
    Wall(map_scaling(21), map_scaling(17)),
    Wall(map_scaling(23), map_scaling(17)),

    Wall(map_scaling(11), map_scaling(19)),
    Wall(map_scaling(13), map_scaling(19)),
    Wall(map_scaling(21), map_scaling(19)),
]
