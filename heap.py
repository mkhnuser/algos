# NOTE: Classical texts use one-based indexing.
# However, I will use zero-based here.


import math
import random


def get_parent_index(i):
    return math.floor((i - 1) / 2)


def get_left_child_index(i):
    return (2 * i) + 1


def get_right_child_index(i):
    return (2 * i) + 2


def max_heapify(A, i):
    lefty = get_left_child_index(i)
    righty = get_right_child_index(i)

    if lefty <= len(A) - 1 and A[lefty] > A[i]:
        largest_index = lefty
    else:
        largest_index = i

    if righty <= len(A) - 1 and A[righty] > A[largest_index]:
        largest_index = righty

    if largest_index != i:
        A[i], A[largest_index] = A[largest_index], A[i]
        max_heapify(A, largest_index)


def build_max_heap(A, n):
    for i in range(math.floor(n / 2), -1, -1):
        max_heapify(A, i)


def is_max_heap_prop_preserved(A, i):
    lefty = get_left_child_index(i)
    righty = get_right_child_index(i)

    if lefty <= len(A) - 1:
        if A[lefty] > A[i]:
            is_lefty_ok = False
        else:
            is_lefty_ok = True
    else:
        is_lefty_ok = True

    if righty <= len(A) - 1:
        if A[righty] > A[i]:
            is_righty_ok = False
        else:
            is_righty_ok = True
    else:
        is_righty_ok = True

    return is_lefty_ok and is_righty_ok


def is_max_heap(A):
    for i in range(len(A)):
        if not is_max_heap_prop_preserved(A, i):
            return False
    return True


if __name__ == "__main__":
    heap_array_sample = [70, 50, 20, 17, 45, 10, 6, 5, 4, 14]
    array = heap_array_sample.copy()
    random.shuffle(array)
    build_max_heap(array, len(array) - 1)
    assert is_max_heap(array)
