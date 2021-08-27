"""

    FIRST BASE FILE FOR BASIC MOVEMENTS

"""

from djitellopy import Tello
from time import sleep

tello = Tello()

tello.connect()
tello.takeoff()

while tello.get_battery() > 20:
    pass

tello.land()