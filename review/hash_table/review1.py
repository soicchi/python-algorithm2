import hashlib


class HashTable:
    def __init__(self, size: int = 10) -> None:
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash(self, key: str) -> str:
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def add(self, key: str, value: any) -> None:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                return

        self.table[index].append([key, value])


if __name__ == "__main__":
    h = HashTable()
    h.add("car", "Tesla")
    h.add("car", "Toyota")
    print(h.table)
