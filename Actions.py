"""
    Complex Actions for Tello Drone
"""

FRAME_X_MAX = 800
FRAME_Y_MAX = 800
SPEED = 30
THRES = 10


def find_clearing_to_land():
    """
        Search for a space on the floor where the drone can land
        for when the battery life is near empty.
    :return:
    """
    # Find a place on the lower half of the screen where there is no identifiable objects
    # Move closer... check again... repeat till height is near 0
    # land and power down
    pass


def explore():
    """
        Search area to map out anything that is unfamiliar.
        Search - forward / side / backward / rarely higher till
            familiarity is really low
    :return:
    """
    pass


"""
    Actions for Specific Object    
"""


def remember(obj="", imgs=None):
    """
        Learn what a specific object looks like (via static images or live stream)
            + correctly classify specific object
    :param obj:
    :param imgs:
    :return:
    """


def find(drone, data, obj=""):
    # find object
    if not data.empty:
        objs = data['name'].str.contains(obj, regex=False)
        if not objs.empty:
            objs = data[objs]

            obj = []
            if len(objs) > 1:
                obj = objs.sort_values(by=['confidence'], ascending=False).iloc[0, :]
            elif len(objs) > 0:
                obj = objs

            if len(obj) > 0:
                print(obj)
                rotate_x = FRAME_X_MAX / 2. - obj['xmax'].values[0]  # neg => counterclockwise rotation
                shift_y = FRAME_Y_MAX / 2. - obj['ymax'].values[0]  # neg => drop in alt.

                # Move to align 'obj' with center
                if shift_y > THRES:
                    drone.down(SPEED)
                elif shift_y < -THRES:
                    drone.up(SPEED)

                if rotate_x > THRES:
                    drone.counter_clockwise(SPEED)
                elif rotate_x < -THRES:
                    drone.clockwise(SPEED)


def move_towards(obj=""):
    pass


def orbit(obj=""):
    pass


def visualize_and_save(frame_, cv2, Output):
    # Convert Image to Color
    img = cv2.cvtColor(frame_[0], cv2.COLOR_RGB2BGR)

    # View Image
    cv2.imshow('Applied CV', img)
    # video writer
    Output.write(cv2.resize(img, (640, 480)))