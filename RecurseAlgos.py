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

