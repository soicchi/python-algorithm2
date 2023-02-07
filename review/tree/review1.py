from __future__ import annotations


class Node:
    def __init__(self, value: int, left: Node = None, right: Node = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def insert(node: Node, value: int) -> None:
    if node is None:
        return Node(value)

    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)

    return node


def inorder(node: Node) -> None:
    if node is None:
        return

    inorder(node.left)
    print(node.value)
    inorder(node.right)

if __name__ == "__main__":
    root = None
    root = insert(root, 3)
    root = insert(root, 6)
    root = insert(root, 5)
    inorder(root)
