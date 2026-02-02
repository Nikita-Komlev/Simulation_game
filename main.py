from abc import ABC, abstractmethod
from collections import deque
from random import randint


class Entity(ABC):
    def __init__(self, location):
        self.location = location

    @property
    @abstractmethod
    def char(self) -> str:
        ...


class Grass(Entity):
    @property
    def char(self) -> str:
        return "G"


class Rock(Entity):
    @property
    def char(self) -> str:
        return "R"


class Tree(Entity):
    @property
    def char(self) -> str:
        return "T"


class Creature(Entity):
    def __init__(self, location, speed, health):
        super().__init__(location)
        self.speed = speed
        self.health = health

    @abstractmethod
    def make_move(self):  # возвращает намерение (следующую клетку / действие)
        ...


class Herbivore(Creature):
    @property
    def char(self) -> str:
        return "H"

    def make_move(self):
        pass


class Predator(Creature):
    def __init__(self, location, speed, health, attack_power):
        super().__init__(location, speed, health)
        self.attack_power = attack_power

    @property
    def char(self) -> str:
        return "P"

    def make_move(self):
        pass


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.entities = dict()

    def add_entity(self, entity):
        ...

    def get_random_cell(self):
        ...

    def passable(self, coord):
        if self.entities.get(coord, None) is None or isinstance(self.entities.get(coord, None), Grass):
            return True
        else:
            return False

    def goal_test(self, creature, coord):  # проверка - является ли текущая клетка соответствующей  целью
        if isinstance(creature, Herbivore) and isinstance(self.entities.get(coord, None), Grass):
            return True
        elif isinstance(creature, Predator) and self.passable(coord) and any(
                isinstance(self.entities.get(neighbor, None), Herbivore) for neighbor in self.neighbors(coord)):
            return True
        else:
            return False

    def neighbors(self, coord):
        neighbors_list = [(coord[0] - 1, coord[1]), (coord[0] + 1, coord[1]), (coord[0], coord[1] + 1),
                          (coord[0], coord[1] - 1)]
        result = list()
        for neighbor in neighbors_list:
            if (neighbor[0] >= 0 and neighbor[0] < self.width) and (neighbor[1] >= 0 and neighbor[1] < self.height):
                result.append(neighbor)
        return result


class Simulation:
    def __init__(self, game_map, render, init_actions=None, turn_actions=None):
        self.map = game_map
        self.render = render
        self.turn_count = 0
        self.is_paused = False
        self.init_actions = init_actions if init_actions is not None else []
        self.turn_actions = turn_actions if turn_actions is not None else []

    def next_turn(self):
        ...

    def start_simulation(self):
        ...

    def pause_simulation(self):
        ...


class Action(ABC):
    @abstractmethod
    def execute(self):
        ...


class SpawnEntities(Action):
    def execute(self):
        ...


class MoveCreatures(Action):
    def execute(self):
        ...


class AddGrass(Action):
    def execute(self):
        ...


class AddHerbivore(Action):
    def execute(self):
        ...


class Render:
    def render(self, game_map):
        ...


class Pathfinder:
    def bfs_next_step(self, map_obj, creature, start):
        queue = deque([start])
        visited = {start}
        parent = {start: None}

        while queue:  # Если очереди нет, цель не найдена
            coord = queue.popleft()  #

            if map_obj.goal_test(creature, coord):
                # Если старт удовлетворен цели - двигаться не нужно
                if coord == start:
                    return None

                current = coord
                while parent[current] != start:
                    current = parent[current]
                    if current is None:
                        return None

                # первый шаг от start
                return current

            for neighbor in map_obj.neighbors(coord):
                if neighbor not in visited and map_obj.passable(neighbor):
                    visited.add(neighbor)
                    parent[neighbor] = coord
                    queue.append(neighbor)
        return None
