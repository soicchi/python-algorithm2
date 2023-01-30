from __future__ import annotations


class Node:
    def __init__(self, data: any, next_node: Node = None, prev_node: Node = None) -> None:
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList:
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
        new_node.prev = current_node

    def insert(self, data: any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def remove(self, data: any) -> None:
        current_node = self.head
        if current_node and current_node.data == data:
            if current_node.next is None:
                self.head = current_node.next
                current_node = None
                return

            next_node = current_node.next
            self.head = next_node
            next_node.prev = None
            current_node = None
            return

        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        previous_node = current_node.prev
        if current_node.next is None:
            previous_node.next = None
            current_node = None
            return

        next_node = current_node.next
        previous_node.next = next_node
        next_node.prev = previous_node
        current_node = None


if __name__ == "__main__":
    d = DoublyLinkedList()
    d.append(1)
    d.append(2)
    d.append(3)
    d.insert(0)
    d.print()
    print("############")
    d.remove(3)
    d.print()