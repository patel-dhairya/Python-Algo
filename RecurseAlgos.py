# Some recursive algorithms written in Python

def reverse_object(obj):
    """
    Returns the reversed object if it is possible
    :param obj: Reference to original object
    :return: Reversed object
    """
    object_type = type(obj)
    empty_object = object_type()

    if obj == empty_object:
        return empty_object

    remain_to_reverse = reverse_object(obj[1:])
    first = obj[:1]

    result = remain_to_reverse + first

    return result


class Ruler:
    """
    For given centimeters and major dash length draw the ruler.
    Algorithm is based on the recursive logic that an interval with central dash length l >= 1 consists:
        1. An interval with central dash length l-1
        2. A single dash of length l
        3. An interval with central dash length l-1
    """

    def __init__(self, centimeters, dash_length):
        self._centimeters = centimeters
        self._dash_length = dash_length

    def set_centimeters(self, centimeters):
        self._centimeters = centimeters

    def set_dash_length(self, dash_length):
        self._dash_length = dash_length

    def draw(self):
        def line_draw(dash_length, number=""):
            line = "-" * dash_length
            if number:
                line += f" {number}"
            print(line)

        def recurse_interval(dash_length):
            if dash_length > 0:
                recurse_interval(dash_length-1)
                line_draw(dash_length)
                recurse_interval(dash_length-1)

        line_draw(self._dash_length, "0")
        for num in range(1, 1 + self._centimeters):
            recurse_interval(self._dash_length - 1)
            line_draw(self._dash_length, str(num))
