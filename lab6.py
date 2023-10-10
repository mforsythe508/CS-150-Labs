##
# Michael Forsythe and Matthew Womack
# Lab 6 lab6.py
# Shortens the length of names to no longer than 10 characters and calculates
# whether someone is a southerner based on distance from Cullowhee and sweet tea preference.
##

CUTOFF = 10
MIN_DISTANCE = 50.0
MAX_DISTANCE = 300.0

def check_name(name: str) -> str:
    """
    Changes name length to be no greater than 10 characters.

    Args:
        name: String representing someone's name.

    Returns:
        A string containing a shortened version of the original name.
    """
    return name[0: CUTOFF]


def check_distance(distance: float) -> float:
    """
    Checks to make sure distance is a positive value.

    Args:
        distance: Float representing the distance from Cullowhee.

    Returns:
        A float containing the distance someone is from Cullowhee.
    """
    if distance < 0:
        distance = 0.0
    return distance

def distance_category(name: str, distance: float) -> str:
    """
    Determines if someone is from nearby, drove, or flew to Cullowhee.

    Args:
        name: String representing someone's name.
        distance: Float representing the distance from Cullowhee.

    Returns:
        A string containing their method of transportation.
    """
    output = ""
    if distance <= MIN_DISTANCE:
        output = name + ", you are from around here!"
    elif distance < MAX_DISTANCE:
        output = name + ", how long did it take to drive?"
    else:
        output = name + ", did you fly?"
    return output

def check_south(tea_fan: bool, distance: float) -> str:
    """
    Determines if someone is a Southerner, almost a Southerner, or not a Southerner.

    Args:
        tea_fan: Boolean representing if someone likes (True) or dislikes (False) sweet tea.
        distance: Float representing the distance from Cullowhee.

    Returns:
        A string containing their Southerner status.
    """
    output = ""
    if tea_fan and distance <= MIN_DISTANCE:
        output = "\tTrue Southerner!\n"
    elif tea_fan or distance <= MIN_DISTANCE:
        output = "\tAlmost a Southerner!\n"
    else:
        output = "\tNot a true Southerner!\n"
    return output

def my_test_lab6() -> None:
    """
    Tests functions through multiples use cases.
    """
    print(check_name("Reese"))
    print(check_name("Eva Mendes"))
    print(check_name("Morgan Freeman"))
    print(check_name("Owen Wilson"))
    print()
    print(check_distance(-6))
    print(check_distance(-0.01))
    print(check_distance(340.1))
    print()
    print(distance_category("Reese", 0.0))
    print(distance_category("Eva Mendes", 50.0))
    print(distance_category("Eva Mendes", 50.1))
    print(distance_category("Morgan Fre", 280))
    print(distance_category("Morgan Fre", 299.9))
    print(distance_category("Owen Wilso", 300.0))
    print(distance_category("Owen Wilso", 340.1))
    print()
    print(check_south(True, 0.0))
    print(check_south(True, 50.01))
    print(check_south(False, 50.0))
    print(check_south(False, 280))

if __name__ == '__main__':
    my_test_lab6()