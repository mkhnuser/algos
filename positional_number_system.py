def obtain_number_from_its_representation(digits: list[int], base: int) -> int:
    """Obtain a number from its representation in a particular base."""

    # NOTE: Python will represent a number in base 10 by default,
    # But the main point is that a NUMBER AS SUCH can be obtained.
    addants = []

    n = 0
    for i in reversed(range(0, len(digits))):
        addants.append(digits[i] * (base**n))
        n += 1

    return sum(addants)


def obtain_number_representation(number: int, base: int) -> str:
    """Obtain a number representation in a particular base."""

    if number == 0:
        return "0"

    remainders = []

    while number > 0:
        number, remainder = divmod(number, base)
        remainders.append(remainder)

    remainders.reverse()
    return "".join(map(str, remainders))


if __name__ == "__main__":
    print(obtain_number_from_its_representation([0], 2))
    print(obtain_number_from_its_representation([1], 2))
    print(obtain_number_from_its_representation([1, 0], 2))
    print(obtain_number_from_its_representation([1, 1], 2))
    print(obtain_number_from_its_representation([1, 1, 1], 2))
    print(obtain_number_from_its_representation([1, 0, 0, 0], 2))

    print(obtain_number_representation(0, 2))
    print(obtain_number_representation(1, 2))
    print(obtain_number_representation(2, 2))
    print(obtain_number_representation(7, 2))
    print(obtain_number_representation(8, 2))
