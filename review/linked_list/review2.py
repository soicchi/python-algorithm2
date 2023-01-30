from __future__ import annotations


class Node:
    def __init__(self, data: any, next_node: Node = None) -> None:
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self, head: Node = None) -> None:
        self.head = head

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def append(self, data: any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node


if __name__ == "__main__":
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.print()