# Tello (Scout Drone)

## Phase 1 (Basics)

In this phase the Tello Scout Drone (aka EITS) will be able to do the following:
- Detect objects in its camera
- Move (towards, away, around) objects
- Follow owner or specified object when told to

### Object Dectection
The initial model will be the pre built / pre optimized YOLOv5 model provided by [Ultralytics](https://github.com/ultralytics/yolov5).
Eventually I'll go back to this model to support my specific use case.

You can see the results of this model with various images under the directory "./results".


## Phase 2 (Learning)
- Learn best path to static objects / areas (via DQL)
- Await commands to perform scout duties (check on 'object' or scout the living room)
- Learn specific object and be able to find / follow the specific object

## Future Improvements
- Improve battery life
- Improve Tello SDK to allow for advanced flight maneuvers and faster frame capture
- Improve hardware for faster speeds / larger flight range / etc
