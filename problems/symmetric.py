"""
Symmetric
Input [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
Output [(5, 3), (7, 4)]
"""

def find_symmetric(pairs: list[tuple[int]]) -> list[tuple[int]]:
    # result = []
    # len_pairs = len(pairs)
    # for i in range(len_pairs):
    #     symmetric = (pairs[i][1], pairs[i][0])
    #     for j in range(i, len_pairs):
    #         if pairs[j] == symmetric:
    #             result.append(pairs[j])

    # return result

    result = []
    cache = {}
    for pair in pairs:
        first, second = pair[0], pair[1]
        value = cache.get(second)
        if value == first:
            result.append((first, second))
        cache[first] = second

    return result


if __name__ == "__main__":
    i = [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
    print(find_symmetric(i))