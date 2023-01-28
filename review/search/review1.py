class Search:
    def recursive_binary_search(self, nums: list[int], target: int) -> int:
        len_nums = len(nums)
        left = 0
        right = len_nums - 1

        target_index = self._binary_search(nums, target, left, right)

        return target_index

    def _binary_search(self, nums: list[int], target: int, left: int, right: int) -> int:
        if left > right:
            return -1

        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        if nums[middle] < target:
            return self._binary_search(nums, target, middle+1, right)

        return self._binary_search(nums, target, left, middle-1)

    def binary_search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
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


if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8,9]
    search = Search()
    print(search.recursive_binary_search(nums, 5))
    print(search.binary_search(nums, 5))