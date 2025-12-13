import os


def find_file(path: str, file_name: str) -> str | None:
    for listing in os.listdir(path):
        path_to_consider = os.path.join(path, listing)

        if os.path.isdir(path_to_consider):
            found_path = find_file(path_to_consider, file_name)
            if found_path is not None:
                return found_path
        else:
            if os.path.basename(path_to_consider) == file_name:
                return path_to_consider


def play_with_dolls(n):
    if n == 0:
        return

    print(f"DOLL'S NUMBER {n} HEAD HAS BEEN DETACHED!")
    play_with_dolls(n - 1)
    print(f"DOLL'S NUMBER {n} HEAD HAS BEEN ATTACHED BACK!")


def find_with_recursive_bin_search(
    left_pointer: int,
    right_pointer: int,
    middle_pointer: int,
    array: list[int],
    target: int,
) -> int | None:
    if left_pointer > right_pointer:
        return

    if array[middle_pointer] == target:
        return middle_pointer
    elif array[middle_pointer] > target:
        right_pointer = middle_pointer - 1
        # NOTE: It's important to include return so that the recursion propagates back successfully.
        return find_with_recursive_bin_search(
            left_pointer,
            right_pointer,
            ((left_pointer + right_pointer) // 2),
            array,
            target,
        )
    else:
        # NOTE: < target
        left_pointer = middle_pointer + 1
        return find_with_recursive_bin_search(
            left_pointer,
            right_pointer,
            ((left_pointer + right_pointer) // 2),
            array,
            target,
        )


def build_stairs(n):
    if n == 0:
        return
    print(n)
    build_stairs(n - 1)


if __name__ == "__main__":
    # print(find_file(str(pathlib.Path.home()), ".alacritty.toml"))
    # play_with_dolls(3)

    # array = [1, 2, 3, 44, 88, 99, 100, 101, 102]
    # array.sort()
    # left_pointer = 0
    # right_pointer = len(array) - 1
    # middle_pointer = (left_pointer + right_pointer) // 2
    # target = -1
    # print(
    #     find_with_recursive_bin_search(
    #         left_pointer,
    #         right_pointer,
    #         middle_pointer,
    #         array,
    #         target,
    #     )
    # )

    # build_stairs(3)
    pass
