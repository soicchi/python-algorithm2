from __future__ import annotations


class Node:
    def __init__(self, data: any, next_node: Node = None) -> None:
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self, head=None) -> None:
        self.head: Node = head

    def append(self, data: any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def insert(self, data: any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data: any) -> None:
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return

        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        previous_node.next = current_node.next
        current_node = None

    def reverse(self) -> None:
        current_node = self.head
        previous_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node

    def reverse_recursive(self) -> None:
        def _reverse_recursive(current_node: Node, previous_node: Node) -> None:
            if not current_node:
                return previous_node

            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            return _reverse_recursive(current_node, previous_node)

        self.head = _reverse_recursive(self.head, None)


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.insert(0)
    linked_list.append(3)
    linked_list.print()
    print("###########")
    linked_list.remove(0)
    linked_list.print()
    print("###########")
    linked_list.reverse()
    linked_list.print()
    print("###########")
    linked_list.reverse_recursive()
    linked_list.print()
