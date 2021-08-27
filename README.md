# Tello (Scout Drone)

## Phase 1 (Basics)

In this phase the Tello Scout Drone (aka EITS) will be able to do the following:
- Detect objects in its camera
- Move (towards, away, around) objects
- Follow owner or specified object when told to

### Object Dectection
The initial model will be YOLOv3 provided by [Jason Brownlee](https://machinelearningmastery.com/how-to-perform-object-detection-with-yolov3-in-keras/).
Eventually I'll go back to this model to support my specific use case.

You can see the results of this model with various images under the directory "./results".


## Phase 2 (Learning)
- Learn best path to static objects / areas (via DQL)
- Await commands to perform scout duties (check on 'object' or scout the living room)

## Future Improvements
- Improve battery life
- Improve SDK to allow for advanced flight maneuvers
- Improve hardware for faster speeds / larger flight range / etc
