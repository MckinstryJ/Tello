"""

    APPLYING CV TO LIVE VIDEO STREAM
    - if video error turn off public firewall

"""
import sys
import traceback
import tellopy
import av
import cv2.cv2 as cv2
import time
import torch
from Actions import *

filename = "C:/Users/McKinstryJohn/Desktop/Python/Tello/vids/output.avi"
codec = cv2.VideoWriter_fourcc("X", "V", "I", "D")
frame_rate = 30
resolution = (640, 480)
Output = cv2.VideoWriter(filename, codec, frame_rate, resolution)

trace_print = False


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
                if trace_print:
                    print(ave)
                    print('retry...')

        frame_skip = 300  # skip first N frames

        drone.takeoff()
        while time.time() - start < 20:
            for frame in container.decode(video=0):
                if 0 < frame_skip:
                    frame_skip = frame_skip - 1
                    continue
                start_time = time.time()

                frame_ = model(frame.to_image())
                # xmin ymin xmax ymax confidence class name
                find(drone, frame_.pandas().xyxy[0], obj)

                # press ESC to end stream
                if cv2.waitKey(1) == 27:
                    break

                if frame.time_base < 1.0 / 60:
                    time_base = 1.0 / 60
                else:
                    time_base = frame.time_base
                frame_skip = int((time.time() - start_time) / time_base)
        drone.land()

    except Exception as ex:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        if trace_print:
            print(ex)
    finally:
        drone.quit()
        cv2.destroyAllWindows()
        Output.release()


if __name__ == '__main__':
    obj = 'person'
    # v5x6 is their current best
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    main()