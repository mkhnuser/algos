# NOTE: This thing works ONLY with type T, not with Any type.
# To put it informally, it's "bound to" type T.
class Stack[T]:
    def __init__(self) -> None:
        self._stack: list[T] = []

    def push(self, item: T) -> None:
        self._stack.append(item)

    def pop(self) -> T | None:
        if self._stack:
            return self._stack.pop()

    def peek(self) -> T | None:
        if self._stack:
            return self._stack[-1]

    def size(self) -> int:
        return len(self._stack)


# NOTE: You can expand it to a Min Max stack.
class StackMaxItem:
    def __init__(self):
        self.items = []
        self.max_items = []

    def push(self, x):
        self.items.append(x)

        if not self.max_items or self.max_items[-1] <= x:
            self.max_items.append(x)

    def pop(self):
        if not self.items:
            return "error"

        popped = self.items.pop()

        if self.max_items[-1] == popped:
            self.max_items.pop()

        return popped

    def get_max(self):
        if not self.max_items:
            return "None"
        return self.max_items[-1]

    def top(self):
        if not self.items:
            return "error"
        return self.items[-1]


if __name__ == "__main__":
    stack = Stack[str]()
    stack.push("banana")
    stack.push("pear")
    stack.push("peach")
    assert stack.pop() == "peach"
    assert stack.peek() == "pear"
    assert stack.peek() == "pear"
    assert stack.pop() == "pear"
    assert stack.peek() == "banana"
