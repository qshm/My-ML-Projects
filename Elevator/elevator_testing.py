import Elevator
from Elevator.wrappers import printlog, logwrap, Timer
from time import sleep

@printlog
def testfunc(arg1u1, arg2, kwarg1='kwarg1', kwarg2='kwarg2'):
    pass


with Timer('mytimer') as t:
    testfunc(11, 22, kwarg1='sdsds', kwarg2='sdsds')
    sleep(2)

    with Timer('mytimer2') as t:


        if __name__ == '__main__':
            elev = Elevator.classes.Elevator(speed=3)
            elev_small = Elevator.classes.SmallElevator(name='ufak')

            elev_slow = elev.slow_elevator()


            # print(elev_small)
            # print(repr(elev))
            # print(repr(elev_small))



            while True:
                try:
                    # destination = None
                    # while not isinstance(destination, int):

                    destination = int(input(f'Which floor do you want to go? Please enter an integer \n'))
                    #
                    elev.stats()

                    elev_small.stats()

                    elev_slow.stats()
                    #
                    #
                    # print(elev.__dict__)
                    #
                    # print(elev_small.__dict__)
                    #
                    # print(elev_small)

                    elev.go_to_floor(destination)
                    elev_small.go_to_floor(destination)
                    elev_slow.go_to_floor(destination)

                    for floor in elev:
                        print('now printing floor: ', floor)

                except ValueError:
                    print("A value error occurred")
                    for item in elev:
                        print(item)
                    break

                except Exception:
                    pass

