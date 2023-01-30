from __future__ import annotations


class Node:
    def __init__(self, data: any, next_node: Node = None, prev_node: Node = None) -> None:
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList:
    def __init__(self, head: Node = None) -> None:
        self.head = head

    def append(self, data: any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        new_node.prev = current_node


if __name__ == "__main__":
    d = DoublyLinkedList()
    d.append(1)
    d.append(2)
    d.append(3)
    print(d.head.data)
    print(d.head.next.data)
    print(d.head.next.next.data)
    print(d.head.next.next.prev.data)
    print(d.head.next.next.prev.prev.data)
