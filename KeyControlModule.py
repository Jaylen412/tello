from djitellopy import tello
import KeyControls as kc
from time import sleep

kc.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())


def getKeyBoardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    # Left and Right
    if kc.getKey('LEFT'):
        lr = -speed
    elif kc.getKey("RIGHT"):
        lr = speed

    # Forward and Back
    if kc.getKey("UP"):
        fb = speed
    elif kc.getKey("DOWN"):
        fb = -speed

    # Up and Down
    if kc.getKey("a"):
        ud = speed
    elif kc.getKey("d"):
        ud = -speed

    # Yaw Left and Yaw Right
    if kc.getKey("z"):
        yv = -speed
    elif kc.getKey("c"):
        yv = speed

    # Takeoff Control
    if kc.getKey("t"):
        drone.takeoff()

    # Land Control
    if kc.getKey("l"):
        drone.land()

    return [lr, fb, ud, yv]


while True:
    vals = getKeyBoardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)
