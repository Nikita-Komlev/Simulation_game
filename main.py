from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, location):
        self.location = location


class Grass(Entity):
    pass


class Rock(Entity):
    pass


class Tree(Entity):
    pass


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
