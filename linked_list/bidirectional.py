from __future__ import annotations


class Node:
    def __init__(
        self,
        data: any,
        next_node: Node = None,
        prev_node: Node = None
    ) -> None:
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

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

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
                self.head = None
                current_node = None
                return
            self.head = current_node.next
            current_node.next.prev = None
            current_node = None
            return


        while current_node and current_node.data != data:
            current_node = current_node.next

        if current_node is None:
            return

        if current_node.next is None:
            current_node.prev.next = None
            current_node = None
            return

        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev
        current_node = None


if __name__ == "__main__":
    dl = DoublyLinkedList()
    dl.append(1)
    dl.append(2)
    dl.append(3)
    dl.insert(0)
    dl.print()
    print("##############")
    dl.remove(2)
    dl.print()
