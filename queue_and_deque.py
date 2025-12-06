from typing import Any


class Q:
    """A rough attempt to implement a queue using a circular buffer."""

    def __init__(self, max_size: int) -> None:
        self.sentinel = object()
        self.size = 0
        self.max_size = max_size
        self.add_pointer = max_size - 1
        self.get_pointer = max_size - 1
        self.items = [self.sentinel for _ in range(max_size)]

    def add(self, item: Any) -> None:
        if self.size >= self.max_size:
            raise Exception("Max size has been exceeded!")

        self.items[self.add_pointer] = item
        self.size += 1

        self.add_pointer -= 1
        self.add_pointer %= self.max_size

    def get(self):
        if not self.size:
            raise Exception("No items!")

        item = self.items[self.get_pointer]
        self.items[self.get_pointer] = self.sentinel
        self.size -= 1

        self.get_pointer -= 1
        self.get_pointer %= 3
        return item


def test_queue():
    q = Q(3)

    q.add(42)
    q.add(5)
    q.add(4)

    try:
        q.add(2345)
    except Exception:
        print("Expected failure to add: max size has been exceeded.")

    assert q.get() == 42
    assert q.get() == 5
    assert q.get() == 4

    try:
        q.get()
    except Exception:
        print("Expected failure to get: there are no items in the queue.")

    q.add(-1)
    q.add(-2)
    q.add(-3)

    try:
        q.add(2345)
    except Exception:
        print("Expected failure to add: max size has been exceeded.")

    try:
        q.add(2345)
    except Exception:
        print("Expected failure to add: max size has been exceeded.")

    assert q.get() == -1
    assert q.get() == -2
    assert q.get() == -3

    try:
        q.get()
    except Exception:
        print("Expected failure to get: there are no items in the queue.")

    try:
        q.get()
    except Exception:
        print("Expected failure to get: there are no items in the queue.")


if __name__ == "__main__":
    test_queue()
