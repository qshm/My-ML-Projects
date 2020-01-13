from abc import ABC, abstractmethod
from Elevator.wrappers import printlog

# abc can not be instantiated itself, subclasses need to implement all abstract methods (override) but can provide
# custom logic via super()
# abc is a form of interface checking more strict than hasattr(), we get error upon instantiation

class ElevatorABC(ABC):

    def __init__(self):
        # speed of elevator in terms of m/s
        self.speed = 1.2
        # distance between each floor in terms of m
        self.distance = 3
        self._available_floors = range(0, 16)

    @abstractmethod
    def stats(self):
        # this method will be provided by inheriting classes
        print('abstract base class method printing')

    @property
    @abstractmethod
    def floor(self):
        # this property will be provided by inheriting classes
        print('abstract base class property printing')
        pass


class Elevator(ElevatorABC):

    def __init__(self):
        super().__init__()
        self._floor = 0
        self.total_time_elapsed = 0
        self.total_distance = 0

        # all floors visited will be kept in the log sequentially
        self.log_floor = []
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.count >= len(self.log_floor):
            raise StopIteration

        self.count += 1

        return self.log_floor[self.count]

    @property
    def floor(self):
        # print('Getting value')
        return self._floor

    @floor.setter
    def floor(self, destination):
        # current_floor = self._floor
        # print(current_floor)

        if destination not in self._available_floors:
            print(f'Available floors are {min(self._available_floors)} to {max(self._available_floors)}')
            raise Exception

        else:
            # print(f'Setting value to {destination}')
            self._floor = destination

    @printlog
    def go_to_floor(self, destination):

        current_floor = self.floor
        self.floor = destination

        if destination == current_floor:
            print(f'You are already on floor {self.floor}')

        else:
            if destination > current_floor:
                print(f'Ascending to: {self.floor}')

            elif destination < current_floor:
                print(f'Descending to: {self.floor}')

            print(f'Congratulations, you arrived at floor {self.floor}')
            self.total_time_elapsed += abs(current_floor - self.floor) * self.distance * self.speed
            self.total_distance += abs(current_floor - destination) * self.distance
            self.log_floor.append(destination)

    def stats(self):
        super().stats()
        print(f'{self.__class__.__name__} travelled {self.total_distance} meters in {self.total_time_elapsed} seconds. \n'
              f' All floors visited: {self.log_floor}')

    # contains as much info about obj as possible to create an accurate representation of the obj
    def __repr__(self):
        return '{!s}({!r},{!r},{!r})'.format(self.__class__.__name__, self.floor, self.total_time_elapsed, self.total_distance)

    # human readable definition of the object.
    def __str__(self):
        return '{} is currently on floor: {}. It has travelled for {} meters'.format(self.__class__.__name__, self.floor, self.total_distance)


class SmallElevator(Elevator):
    # demonstrates inheritance

    def __init__(self, *, name=None):

        # call __init__ on subclass as seen by the superclass
        super().__init__()

        self.speed = 1.1
        self._available_floors = range(0, 9)

        # name is an optional keyword argument, created as an attribute only when given.
        # Demonstrates added functionality to subclass without breaking existing function calls

        if name is not None:
            self.name = name

    # override parent's __repr__ method (Default Implementation of __repr__)
    def __repr__(self):
        return '<{0}.{1} object at {2}>'.format(self.__module__, type(self).__name__, hex(id(self)))

    def stats(self):
        if hasattr(self, 'name'):
            print(f'{self.name} travelled {self.total_distance} meters in {self.total_time_elapsed} seconds. \n'
                  f' All floors visited: {self.log_floor}')
        else:
            super(SmallElevator, self).stats()

        # todo: multiple inheritance, encapsulation?
