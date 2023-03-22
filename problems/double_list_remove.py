"""
Input: X: [1,2,3,4,4,5,5,8,10] Y:[4,5,5,5,6,7,8,8,10]
Output: X: [1,2,3,4,4,10] Y: [5,5,5,6,7,8,8,10]
"""

from collections import Counter
import time


def remove_less(X: list[int], Y: list[int]) -> None:
    start = time.time()
    counter_x = Counter(X)
    counter_y = Counter(Y)

    for x_key, x_val in counter_x.items():
        y_val = counter_y.get(x_key)
        if y_val is None:
            continue
        if x_val < y_val:
            X[:] = [i for i in X if i != x_key]
        elif x_val > y_val:
            Y[:] = [j for j in Y if j != x_key]

    print(time.time() - start)

if __name__ == "__main__":
    X = [1,2,3,4,4,5,5,8,10]
    Y = [4,5,5,5,6,7,8,8,10]
    remove_less(X, Y)
    print(X)
    print(Y)