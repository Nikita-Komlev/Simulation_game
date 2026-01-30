from abc import ABC, abstractmethod
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
