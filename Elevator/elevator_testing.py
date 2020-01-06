import Elevator

if __name__ == '__main__':
    elev = Elevator.classes.Elevator()
    elev_small = Elevator.classes.SmallElevator()


    while True:
        try:
            # destination = None
            # while not isinstance(destination, int):

            destination = int(input(f'Which floor do you want to go? Please enter an integer \n'))
            elev.go_to_floor(destination)

            elev_small.go_to_floor(destination)

            elev.stats()

            elev_small.stats()

            print(elev.__dict__)
            print(elev_small.__dict__)

        except ValueError:
            print("A value error occurred")

        except Exception:
            pass
