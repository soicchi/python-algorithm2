class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


def insert(node: Node, value: int) -> Node:
    if node is None:
        return Node(value)

    if value < node.value:
        node.left = insert(node.left, value)
        return node

    node.right = insert(node.right, value)
    return node


def inorder(node: Node) -> None:
    # Inorder: left, root, right
    # preorder: root, left, right
    # Postorder: left, right, root
    if node is None:
        return

    inorder(node.left)
    print(node.value)
    inorder(node.right)


def search(node: Node, value: int) -> bool:
    if node is None:
        return False

    if node.value == value:
        return True

    if node.value > value:
        return search(node.left, value)

    return search(node.right, value)


if __name__ == "__main__":
    root = None
    root = insert(root, 3)
    root = insert(root, 6)
    root = insert(root, 5)
    root = insert(root, 7)
    root = insert(root, 1)
    root = insert(root, 10)
    root = insert(root, 2)
    inorder(root)
    print(search(root, 8))
