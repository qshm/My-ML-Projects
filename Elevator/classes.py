import time


class Elevator:
    # speed of elevator in terms of m/s
    speed = 1.2

    # distance between each floor in terms of m
    distance = 3

    _available_floors = range(0, 16)

    def __init__(self):
        self._floor = 0
        self.total_time_elapsed = 0
        self.total_distance = 0

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

    def stats(self):
        print(f'{self.total_distance} meters travelled in {self.total_time_elapsed} seconds')


class SmallElevator(Elevator):
    speed = 1.1
    _available_floors = range(0, 9)

    def __init__(self, *, name=None):
        self._floor = 0
        self.total_time_elapsed = 0
        self.total_distance = 0

        # name is an optional keyword argument, created as an attribute only when given.
        # Demonstrates added functionality to subclass without breaking existing function calls

        if not name == None:
            self.name = name

    def stats(self):
        if not hasattr(self, 'name'):
            name = 'New elevator'
        else:
            name = self.name
        print(f'{name} travelled {self.total_distance} meters in {self.total_time_elapsed} seconds')