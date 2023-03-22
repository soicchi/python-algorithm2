"""
Input: 'This is a pen. This is apple. Applepen'
Output: ('p', 6)
"""

import operator
from collections import Counter


def find_most_string(sentence: str) -> tuple[str, int]:
    sentence = sentence.lower()
    # l = []
    # for char in sentence:
    #     if not char.isspace():
    #         l.append((char, sentence.count(char)))

    l = [(c, sentence.count(c)) for c in sentence if not c.isspace()]
    return max(l, key=operator.itemgetter(1))


def find_most_string_v2(strings: str) -> tuple[str, int]:
    strings = strings.lower()
    cache = {}
    for char in strings:
        if not char.isspace():
            cache[char] = cache.get(char, 0) + 1

    max_key = max(cache, key=cache.get)
    return max_key, cache[max_key]


def find_most_string_v3(strings: str) -> tuple[str, int]:
    strings = strings.lower()
    cache = Counter()
    for char in strings:
        if not char.isspace():
            cache[char] += 1

    max_key = max(cache, key=cache.get)
    return max_key, cache[max_key]


if __name__ == "__main__":
    i = "This is a pen. This is apple. Applepen"
    print(find_most_string(i))
    print(find_most_string_v2(i))
    print(find_most_string_v3(i))