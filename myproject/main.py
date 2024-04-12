def division(number_1: int, number_2: int) -> int:
    """Returns division of two numbers
    :param number_1: First number
    :param number_2: Second number
    :return: Division of two numbers"""

    return int(number_1 / number_2)


def signature(number: float) -> int:
    """
    Return 1 if positive, -1 if negative, 0 if zero
    :param number:
    :return: Signature of the number: int
    """
    if number == 0:
        return 0
    elif number > 0:
        return 1
    else:
        return -1


class SampleClass:
    def __init__(self, value):
        self.value = value
