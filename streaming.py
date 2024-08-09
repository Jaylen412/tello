from djitellopy import tello
import cv2

# Connecting to drone
drone = tello.Tello()
drone.connect()
print(drone.get_battery())

# Activating stream
drone.streamon()

while True:
    video = drone.get_frame_read().frame
    # video = cv2.resize(video, (300, 240))
    cv2.imshow("Video", video)
    cv2.waitKey(1)
