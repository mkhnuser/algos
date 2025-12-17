import random


def merge_sort(array):
    if len(array) == 0 or len(array) == 1:
        return array

    middle = len(array) // 2
    sorted_left_part = merge_sort(array[:middle])
    sorted_right_part = merge_sort(array[middle:])

    # NOTE: It is better to preallocate the full size.
    res = []
    i = 0
    j = 0

    while i < len(sorted_left_part) and j < len(sorted_right_part):
        left_el = sorted_left_part[i]
        right_el = sorted_right_part[j]
        if left_el <= right_el:
            res.append(left_el)
            i += 1
        else:
            res.append(right_el)
            j += 1

    while i < len(sorted_left_part):
        left_el = sorted_left_part[i]
        i += 1
        res.append(left_el)

    while j < len(sorted_right_part):
        right_el = sorted_right_part[j]
        j += 1
        res.append(right_el)

    return res


def quick_sort(array):
    if len(array) in (0, 1):
        return array

    pivot = random.choice(array)
    less_than = [el for el in array if el < pivot]
    equal_to = [el for el in array if el == pivot]
    more_than = [el for el in array if el > pivot]

    return quick_sort(less_than) + equal_to + quick_sort(more_than)


def counting_sort(nums):
    # NOTE: Counting Sort works when you need to sort elements
    # Which are in range [0, k).
    range_ = [0] * 12

    for num in nums:
        range_[num] += 1

    output = []

    for number in range(len(range_)):
        output.extend([number] * range_[number])

    return output


def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
    return array


if __name__ == "__main__":
    array = [-1, 1, -1, 1, -1, 10, 0, 42, 39, 87, 7, 0, 0]
    # print(merge_sort(array))
    # print(quick_sort(array))
    nums = [5, 7, 1, 0, 1, 5, 11, 1]
    print(counting_sort(nums))
