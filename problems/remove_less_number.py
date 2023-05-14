'''
Input X: [1, 2, 3, 4, 4, 5, 5, 8, 10] Y: [4, 5, 5, 5, 6, 7, 8, 8, 10]
=>    X: [1, 2, 3, 4, 4, 10]          Y: [5, 5, 5, 6, 7, 8, 8, 10]
'''

from collections import Counter


def remove_less_num(x: list[int], y: list[int]) -> None:
    # xの数値の出現個数を追跡する辞書counter_xを初期化
    counter_x = Counter(x)

    # yの数値の出現個数を追跡する辞書counter_yを初期化
    counter_y = Counter(y)

    # counter_xをkey_x, value_xで走査
    for key_x, value_x in counter_x.items():

        # counter_yにkey_xに該当するvalue_yを生成
        value_y = counter_y.get(key_x, 0)

        # value_x < value_yの場合
        if value_x < value_y:

            # xをインプレースでリスト内から該当する数値を削除
            x[:] = [num for num in x if num != key_x]

        # value_x > value_yの場合
        elif value_x > value_y:

            # yをインプレースでリスト内から該当する数値を削除
            y[:] = [num for num in y if num != key_x]


def remove_less_num2(x: list[int], y: list[int]) -> None:
    counter_x = Counter(x)
    counter_y = Counter(y)

    remove_nums_from_x = {key for key, value in counter_x.items() if value < counter_y.get(key, 0)}
    remove_nums_from_y = {key for key, value in counter_y.items() if value < counter_x.get(key, 0)}

    x[:] = [num for num in x if num not in remove_nums_from_x]
    y[:] = [num for num in y if num not in remove_nums_from_y]


if __name__ == '__main__':
    x = [1, 2, 3, 4, 4, 5, 5, 8, 10]
    y = [4, 5, 5, 5, 6, 7, 8, 8, 10]
    remove_less_num2(x, y)
    print(x)
    print(y)
