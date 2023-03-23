"""
[1] -> [2] -> 2
[2, 3] -> [2, 4] -> 24
[8, 9] -> [9, 0] -> 90
[9, 9, 9] -> [1, 0, 0, 0] -> 1000
[0, 0, 0, 9, 9, 9] -> [1, 0, 0, 0] -> 1000
"""


def list_to_int(nums: list[int]) -> int:
    sum_nums = 0
    for i, num in enumerate(reversed(nums)):
        sum_nums += num * (10 ** i)
    return sum_nums


def remove_zero(nums: list[int]) -> None:
    if nums and nums[0] == 0:
        nums.pop(0)
        remove_zero(nums)


def plus_one(nums: list[int]) -> int:
    end = len(nums) - 1
    nums[end] += 1
    while end > 0:
        if nums[end] != 10:
            remove_zero(nums)
            return list_to_int(nums)
        nums[end] = 0
        nums[end-1] += 1
        end -= 1

    remove_zero(nums)
    nums[end] = 1
    nums.append(0)
    return list_to_int(nums)


if __name__ == "__main__":
    nums = [9,9,9]
    print(plus_one(nums))
