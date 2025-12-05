from typing import Any


class Node:
    def __init__(self, value: Any, next: "Node | None") -> None:
        self.value = value
        self.next = next


# WARNING: One-based counting is assumed, not zero-based.


class LinkedList:
    @staticmethod
    def print_list(vertex: Node):
        # NOTE: Perhaps, you want to provide head here.
        current_node = vertex

        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    @staticmethod
    def insert_node(head: Node, vertex: Node, index: int) -> None:
        # NOTE: Possible options are:
        # 1. Insertion as a first element.
        # 2. Insertion somewhere in the middle.
        # 3. Insertion at the end.
        # 2. and 3. are handled the same.

        if index < 1:
            raise ValueError(f"Out of bound index {index} has been provided.")

        if index == 1:
            vertex.next = head
            return

        # NOTE: Assume natural counting is used:
        # You count nodes from 1 onward.
        # If you want insert something, you do it "before" the node position.

        counter = 2
        current_node = head

        while current_node is not None:
            if counter == index:
                # NOTE: current -> v -> next.
                vertex.next = current_node.next
                current_node.next = vertex
                return

            current_node = current_node.next
            counter += 1

        raise ValueError(f"Out of bound index {index} has been provided.")

    @staticmethod
    def delete_node(head: Node, index: int) -> Node | None:
        if index < 1:
            raise ValueError("Invalid Index has been provided!")

        if index == 1:
            new_head = head.next
            return new_head

        node = head
        index -= 2

        while index and node is not None:
            node = node.next
            index -= 1

        if node is None:
            raise ValueError("Invalid Index has been provided!")

        node_to_be_deleted = node.next

        if node_to_be_deleted is None:
            raise ValueError("Invalid Index has been provided!")

        node.next = node_to_be_deleted.next
        return head


if __name__ == "__main__":
    third_node = Node(value=3, next=None)
    second_node = Node(value=2, next=third_node)
    head = Node(value=1, next=second_node)

    linked_list = LinkedList()
    # linked_list.print_list(head)

    new_node = Node(value="inserted", next=None)
    # linked_list.insert_node(head, new_node, 1)
    # linked_list.insert_node(head, new_node, 2)
    # linked_list.insert_node(head, new_node, 5)

    # try:
    #     linked_list.insert_node(head, new_node, 999)
    # except ValueError:
    #     print("ValueError has occured.")
    #     pass

    # new_head = linked_list.delete_node(head, 1)
    new_head = linked_list.delete_node(head, 4)
    if new_head is not None:
        linked_list.print_list(new_head)
