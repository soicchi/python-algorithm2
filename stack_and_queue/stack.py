class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, data: any) -> None:
        self.stack.append(data)

    def pop(self) -> any:
        if self.stack:
            return self.stack.pop()


if __name__ == "__main__":
    s = Stack()
    print(s.stack)
    s.push(1)
    print(s.stack)
    print(s.pop())
    print(s.stack)
