"""
Sorting algorithms implemented in Python
"""
from collections.abc import Hashable
import random


def insertion_sort(arr: list) -> list:
    """
    Sort the list with insertion sort algorithm
    :param arr: List
    :return: Sorted List
    """
    if len(arr) == 0:
        return arr
    # check if elements in array can be compared with each other
    if not isinstance(arr[0], Hashable):
        raise TypeError("List elements do not have comparison property")

    for index_i in range(1, len(arr)):
        current_element_index = index_i
        while current_element_index > 0 and \
                arr[current_element_index] < arr[current_element_index - 1]:
            arr[current_element_index], arr[current_element_index - 1] = \
                arr[current_element_index - 1], arr[current_element_index]
            current_element_index -= 1
    return arr


def selection_sort(arr: list) -> list:
    """
        Sort the list with selection sort algorithm
        :param arr: List
        :return: Sorted List
        """
    if len(arr) == 0:
        return arr
    # check if elements in array can be compared with each other
    if not isinstance(arr[0], Hashable):
        raise TypeError("List elements do not have comparison property")

    for index_i in range(len(arr)):
        current_smallest_element_index = arr.index(min(arr[index_i:]))
        arr[current_smallest_element_index], arr[index_i] = \
            arr[index_i], arr[current_smallest_element_index]
    return arr
