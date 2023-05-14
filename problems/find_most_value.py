'''
Input: 'This is a pen. This is an apple. Applepen.'
Output: ('p', 6)
'''


import operator
from collections import Counter


# pattern1
def find_most_frequency(sentence: str) -> tuple[str, int]:
    # 各文字の出現数を追跡する辞書char_frequencyを初期化
    char_frequency = []

    # sentenceのすべての文字列を小文字に置き換える
    sentence = sentence.lower()

    # sentenceを小文字に置き換えて走査
    for char in sentence:

        # char_frequencyに現在の値がkeyとして存在すれば、valueを1つ増やしなければ1で初期化
        if not char.isspace():
            char_frequency.append((char, sentence.count(char)))

    # max関数を利用し、最も多く出現した文字列を返す
    return max(char_frequency, key=operator.itemgetter(1))


# pattern2
def find_most_frequency2(sentence: str) -> tuple[str, int]:
    char_frequency = Counter()

    for char in sentence.lower():
        if not char.isspace():
            char_frequency[char] += 1

    char, frequency = char_frequency.most_common(1)[0]
    return (char, frequency)


if __name__ == '__main__':
    sentence = 'This is a pen. This is an apple. Applepen.'
    # print(find_most_frequency(sentence))
    print(find_most_frequency2(sentence))
