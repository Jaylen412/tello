from djitellopy import tello
import KeyControls as kc
import time
import cv2


global video
kc.init()
drone = tello.Tello()

# Connect to Tello
drone.connect()

# Activating stream
drone.streamon()


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
        time.sleep(3)
        drone.land()

    # Take picture
    if kc.getKey("m"):
        cv2.imwrite(f'resources/images{time.time()}.jpg', video)
        time.sleep(0.3)

    # Emergency
    if kc.getKey("e"):
        drone.emergency()

    return [lr, fb, ud, yv]


while True:
    vals = getKeyBoardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    video = drone.get_frame_read().frame
    cv2.imshow("Video", video)
    cv2.waitKey(1)

