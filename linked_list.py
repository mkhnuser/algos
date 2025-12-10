class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def print_list(node):
    while node is not None:
        print(node.value)
        node = node.next


def insert_node(head, node, index):
    # NOTE: Return a new node.
    if index == 0:
        node.next = head
        return node

    assert index >= 1
    initial_head = head
    index -= 1

    while head is not None and index > 0:
        head = head.next
        index -= 1

    if head is None:
        raise Exception("Out of range!")

    prev_next = head.next
    head.next = node
    node.next = prev_next
    return initial_head


def delete_node(head, index):
    if index == 0:
        return head.next

    assert index >= 1
    index -= 1
    initial_head = head

    while head is not None and index > 0:
        head = head.next
        index -= 1

    if head is None:
        raise Exception("Out of range!")

    to_be_deleted = head.next

    if to_be_deleted is None:
        raise Exception("Out of range!")

    head.next = to_be_deleted.next
    return initial_head


if __name__ == "__main__":
    first = Node(value=1)
    second = Node(value=2)
    third = Node(value=3)
    fourth = Node(value=4)

    first.next = second
    second.next = third
    third.next = fourth

    new_head = delete_node(first, 0)
    print_list(new_head)
