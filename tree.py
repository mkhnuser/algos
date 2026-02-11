# NOTE: Two possible implementations of a Node follow.


class Node:
    def __init__(self, obj, children=None):
        # NOTE: Recall that a node might have a near infinate number of children.
        self.obj = obj
        if children is not None:
            self.children = children
        else:
            self.children = []


class Node:
    def __init__(self, obj, left=None, right=None):
        # NOTE: This is, howerver, an example of a "binary" node.
        self.obj = obj
        self.left = left
        self.right = right


def find_node_by_value(root, value):
    return recurse_find_node_by_value(root, value)


def recurse_find_node_by_value(node, value):
    if node is None:
        return None

    if node.value == value:
        return node

    if value < node.value:
        return recurse_find_node_by_value(node.left, value)
    else:
        return recurse_find_node_by_value(node.right, value)


def print_forward(node):
    # NOTE: This method works for any tree.
    print(node.obj)
    for child in node.children:
        print_forward(child)


def print_reversed(node):
    # NOTE: This method works for any tree.
    for child in node.children:
        print_reversed(child)
    print(node.obj)


def print_LMR(vertex):
    # NOTE: This method works only for binary trees.
    # This also prints elements in sorted order: from the smallest to the biggest.
    if vertex.left is not None:
        print_LMR(vertex.left)

    print(vertex.obj)

    if vertex.right is not None:
        return print_LMR(vertex.right)


def insert_node(root, node):
    return recurse_insert_node(root, node)


def recurse_insert_node(root, node):
    if node.obj < root.obj:
        if root.left is None:
            root.left = node
        else:
            recurse_insert_node(root.left, node)
    else:
        if root.right is None:
            root.right = node
        else:
            recurse_insert_node(root.right, node)


def test_traversal_of_nary_tree():
    node_g = Node("G")
    node_h = Node("H")
    node_i = Node("I")
    node_f = Node("F")
    node_c = Node("C")
    node_d = Node("D")
    node_e = Node("E", children=[node_g, node_h, node_i])
    node_b = Node("B", children=[node_e, node_f])
    node_a = Node("A", children=[node_b, node_c, node_d])
    print_reversed(node_a)


def bfs(node, needle):
    to_be_visited = []
    to_be_visited.append(node)

    while to_be_visited:
        v = to_be_visited.pop()

        if v.obj == needle:
            return True

        for child in v.children:
            to_be_visited.append(child)

    return False


def dfs(node, needle) -> bool:
    # NOTE: This has no assumption that we are dealing with a BST.
    if node.obj == needle:
        return True

    for child in node.children:
        if dfs(child, needle):
            return True

    return False


def test_bfs_for_nary_tree():
    #                    A
    #       B            C             D
    #   E       F
    #  GHI

    node_g = Node("G")
    node_h = Node("H")
    node_i = Node("I")
    node_f = Node("F")
    node_c = Node("C")
    node_d = Node("D")
    node_e = Node("E", children=[node_g, node_h, node_i])
    node_b = Node("B", children=[node_e, node_f])
    node_a = Node("A", children=[node_b, node_c, node_d])
    print(bfs(node_a, "G"))


def test_dfs_for_nary_tree():
    #                    A
    #       B            C             D
    #   E       F
    #  GHI

    node_g = Node("G")
    node_h = Node("H")
    node_i = Node("I")
    node_f = Node("F")
    node_c = Node("C")
    node_d = Node("D")
    node_e = Node("E", children=[node_g, node_h, node_i])
    node_b = Node("B", children=[node_e, node_f])
    node_a = Node("A", children=[node_b, node_c, node_d])
    print(dfs(node_a, "G"))


if __name__ == "__main__":
    pass
