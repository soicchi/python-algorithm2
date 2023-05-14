'''
Symmetric
Input [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
Output [(5, 3), (7, 4)]
'''

from typing import Iterator


# pattern1
def find_symmetric(pairs: list[tuple[int, int]]) -> list[tuple[int, int]]:
    # 組み合わせを追跡する辞書cacheを初期化
    cache = {}
    symmetric_pairs = []

    # pairsを走査
    for pair in pairs:

        # cacheのkeyに現在の値がある場合
        if pair in cache:

            # 現在の値とcacheに格納されているvalueをリスト形式で返す
            symmetric_pairs.append(pair)

        # cacheのkeyに反対の値、valueに現在の値を格納
        reversed_pair = (pair[1], pair[0])
        cache[reversed_pair] = pair

    return symmetric_pairs


# pattern2
def find_symmetric2(pairs: list[tuple[int, int]]) -> Iterator[tuple[int, int]]:
    cache = {}

    for pair in pairs:
        # 現在の値をそれぞれfirst, secondに格納する
        first, second = pair[0], pair[1]
        value = cache.get(second)

        if not value:
            cache[first] = second
        elif value == first:
            yield pair


if __name__ == '__main__':
    pairs = [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
    # print(find_symmetric2(pairs))
    for r in find_symmetric2(pairs):
        print(r)
