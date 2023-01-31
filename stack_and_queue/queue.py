from collections import deque


class Queue:
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, data: any) -> None:
        self.queue.append(data)

    def dequeue(self) -> any:
        if self.queue:
            return self.queue.pop(0)


if __name__ == "__main__":
    q = deque()
    # q.enqueue(1)
    # print(q.queue)
    # q.dequeue()
    # print(q.queue)
    q.append(1)
    q.append(2)
    q.append(3)
    print(q)
    q.popleft()
    print(q)