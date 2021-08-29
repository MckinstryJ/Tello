"""

    APPLYING CV TO LIVE VIDEO STREAM

"""
from djitellopy import Tello
import cv2


def main():
    tello = Tello()
    tello.connect()

    tello.streamoff()
    tello.streamon()

    frame_read = tello.get_frame_read()
    while tello.get_battery() > 20:
        frame = frame_read.frame
        cv2.imshow('Video', frame)
        cv2.waitKey(1000)


if __name__ == "__main__":
    main()