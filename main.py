"""

    APPLYING CV TO LIVE VIDEO STREAM
    - if video error turn off public firewall

"""
import sys
import traceback
import tellopy
import av
import cv2.cv2 as cv2  # for avoidance of pylint error
import numpy as np
import time
import torch

filename = "C:/Users/McKinstryJohn/Desktop/Python/Tello/vids/output.avi"
codec = cv2.VideoWriter_fourcc("X", "V", "I", "D")
frame_rate = 30
resolution = (640, 480)
Output = cv2.VideoWriter(filename, codec, frame_rate, resolution)


def main():
    drone = tellopy.Tello()
    start = time.time()

    try:
        drone.connect()
        drone.wait_for_connection(60.0)

        retry = 3
        container = None
        while container is None and 0 < retry:
            retry -= 1
            try:
                container = av.open(drone.get_video_stream())
            except av.AVError as ave:
                print(ave)
                print('retry...')

        # skip first 300 frames
        frame_skip = 300
        while time.time() - start < 20:
            for frame in container.decode(video=0):
                if 0 < frame_skip:
                    frame_skip = frame_skip - 1
                    continue
                start_time = time.time()

                img = model(frame.to_image()).render()[0]
                img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

                cv2.imshow('Applied CV', img)
                # video writer
                Output.write(cv2.resize(img, (640, 480)))

                # press ESC to end stream
                if cv2.waitKey(1) == 27:
                    break

                if frame.time_base < 1.0 / 60:
                    time_base = 1.0 / 60
                else:
                    time_base = frame.time_base
                frame_skip = int((time.time() - start_time) / time_base)

    except Exception as ex:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        print(ex)
    finally:
        drone.quit()
        cv2.destroyAllWindows()
        Output.release()


if __name__ == '__main__':
    # v5x6 is their current best
    model = torch.hub.load('ultralytics/yolov5', 'yolov5x6')
    main()