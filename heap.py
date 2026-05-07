class MinHeap[T]:
    def __init__(self):
        self.data = []  # NOTE: This array will be preserve min heap property.

    def insert(self, datum: T) -> None:
        """Insert an element into a min heap."""
        # NOTE: Append to the end.
        # Sift up.
        self.data.append(datum)
        self._sift_up(len(self.data) - 1)

    def delete(self) -> T:
        """Delete the min element from a min heap."""
        # NOTE: Pop the root.
        # Put the last element at the root.
        # Sift it down.
        # Return the popped root.
        if not self.data:
            raise Exception("The heap is empty.")

        out = self.data[0]
        new_root = self.data.pop()

        if not self.data:
            # NOTE: The out element was the only element present in the heap.
            return out

        self.data[0] = new_root
        self._sift_down(0)
        return out

    def _sift_up(self, index: int) -> None:
        if index == 0:
            return

        parent_index = self._get_parent_index(index)
        parent_element = self.data[parent_index]
        current_element = self.data[index]

        if parent_element > current_element:
            self.data[parent_index], self.data[index] = (
                self.data[index],
                self.data[parent_index],
            )
            self._sift_up(parent_index)

    def _sift_down(self, index: int) -> None:
        if index >= len(self.data):
            return

        left_child_index = self._get_left_child_index(index)
        right_child_index = self._get_right_child_index(index)
        min_element_index = index

        if (
            left_child_index < len(self.data)
            and self.data[left_child_index] < self.data[min_element_index]
        ):
            min_element_index = left_child_index
        if (
            right_child_index < len(self.data)
            and self.data[right_child_index] < self.data[min_element_index]
        ):
            min_element_index = right_child_index

        if min_element_index != index:
            self.data[min_element_index], self.data[index] = (
                self.data[index],
                self.data[min_element_index],
            )
            self._sift_down(min_element_index)

    def _get_parent_index(self, index: int) -> int:
        return (index - 1) // 2

    def _get_left_child_index(self, index: int) -> int:
        return (2 * index) + 1

    def _get_right_child_index(self, index: int) -> int:
        return (2 * index) + 2


def test_min_heap():
    min_heap = MinHeap()

    for element in (33, 21, 56, 5, 19, 18, 20):
        min_heap.insert(element)

    assert min_heap.delete() == 5
    assert min_heap.delete() == 18
    assert min_heap.delete() == 19
    assert min_heap.delete() == 20
    assert min_heap.delete() == 21
    assert min_heap.delete() == 33
    assert min_heap.delete() == 56


if __name__ == "__main__":
    test_min_heap()
