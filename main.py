from abc import ABC, abstractmethod


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
    def make_move(self):
        raise NotImplementedError


class Herbivore(Creature):
    def make_move(self):
        pass


class Predator(Creature):
    def __init__(self, location, speed, health, power):
        super().__init__(location, speed, health)
        self.power = power

    def make_move(self):
        pass
