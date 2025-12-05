"""Play here!"""

from typing import Any


class Node:
    def __init__(self, value: Any, next: "Node | None") -> None:
        self.value = value
        self.next = next


def get_node_by_index(node, index):
    while index:
        node = node.next
        index -= 1
    return node


def insert_node(head, index, value):
    # NOTE: Insert a new node and return head!

    new_node = Node(value=value, next=None)

    if index == 0:
        new_node.next = head
        return new_node

    # NOTE: index = 1 => index - 1 = 0 => prev node is head.
    # index = 2 => index - 1 = 1 => prev node is head + 1.
    # a -> b -> c -> None.
    previous_node = get_node_by_index(head, index - 1)
    new_node.next = previous_node.next
    previous_node.next = new_node
    return head


def print_list(vertex: Node):
    # NOTE: Perhaps, you want to provide head here.
    current_node = vertex

    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next


if __name__ == "__main__":
    third_node = Node(value=3, next=None)
    second_node = Node(value=2, next=third_node)
    head = Node(value=1, next=second_node)

    print_list(head)
    insert_node(head, 3, "inserted")
    print_list(head)
