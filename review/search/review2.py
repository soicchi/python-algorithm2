from typing import NewType


IndexNum = NewType("IndexNum", int)


class Search:
    def binary_search(self, nums: list[int], target: int) -> IndexNum:
        left, right = 0, len(nums)-1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                left = middle + 1
                continue
            if nums[middle] > target:
                right = middle - 1
                continue

        return -1

    def binary_search_recursive(self, nums: list[int], target: int) -> IndexNum:
        def _binary_search(nums: list[int], target: int, left: IndexNum, right: IndexNum) -> IndexNum:
            if left > right:
                return -1

            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                return _binary_search(nums, target, middle+1, right)

            return _binary_search(nums, target, left, middle-1)

        target_index = _binary_search(nums, target, 0, len(nums)-1)

        return target_index


if __name__ == "__main__":
    nums = [1,2,3,4,5,6]
    s = Search()
    print(s.binary_search(nums, 2))
    print(s.binary_search_recursive(nums, 2))