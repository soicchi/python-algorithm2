from typing import Optional


"""
1. Input [11, 2, 5, 9, 10, 3], 12 => Output: (2, 10) or None
2. Input [11, 2, 5, 9, 10, 3]     => Output: (11, 9) or None  ex) 11 + 9 = 2 + 5 + 10 +3
"""

def quiz1(nums: list[int], target: int) -> Optional[tuple[int]]:
    cache = set()
    for num in nums:
        val = target - num
        if val in cache:
            return val, num
        cache.add(num)


def quiz2(nums: list[int]) -> Optional[tuple[int]]:
    half, rest_val = divmod(sum(nums), 2)
    if rest_val != 0:
        return
    cache = set()
    for num in nums:
        val = half - num
        if val in cache:
            return val, num
        cache.add(num)


if __name__ == "__main__":
    nums = [11,2,5,9,10,3]
    target = 12
    print(quiz1(nums, target))
    print(quiz2(nums))