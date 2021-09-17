"""
    Complex Actions for Tello Drone
"""


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


def find(obj=""):
    pass


def move_towards(obj=""):
    pass


def orbit(obj=""):
    pass