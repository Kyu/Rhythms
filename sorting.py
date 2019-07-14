from random import randint, seed

from helpers import timeit


def create_array(array_length=50):
    seed(a=None, version=2)
    array = [0] * array_length
    array = [randint(0, 500) for i in array]

    return array


@timeit
def bubble_sort(array_length=50):
    array = create_array(array_length)
    print("Array: \n", array)

    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]

    print("Bubble Sorted Array: \n", array)


# TODO: Doesn't work, also add
@timeit
def merge_sort(array_length=None, array=None, benchmark=False):
    if array_length:
        array = create_array(array_length)
        print("Array: \n", array)

    mid = len(array) // 2

    if mid == 1:
        if array[1] < array[0]:
            array[0], array[1] = array[1], array[0]
        return array
    if mid < 1:
        return array

    left, right = merge_sort(array=array[0:mid]), merge_sort(array=array[mid:len(array)])

    if len(left) == len(right):
        pass

    for i in range(len(left)):
        if left[i] < right[i]:
            left[i], right[i] = right[i], left[i]

    return left + right
