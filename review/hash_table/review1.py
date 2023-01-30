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

    def get(self, key: str) -> any:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]

    def __setitem__(self, key: str, value: any) -> None:
        self.add(key, value)

    def __getitem__(self, key: str) -> any:
        return self.get(key)


if __name__ == "__main__":
    h = HashTable()
    h["car"] = "Tesla"
    h["car"] = "Toyota"
    print(h.table)
    print(h["car"])
