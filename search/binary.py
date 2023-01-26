class Search:
    def binary_search(self, nums: list[int], target: int) -> int:
        len_nums = len(nums)
        left, right = 0, len_nums-1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1

    def recursive_binary_search(self, nums: list[int], target: int) -> int:
        def _binary_search(nums: list[int], target: int, left: int, right: int) -> int:
            if left > right:
                return -1

            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                return _binary_search(nums, target, middle+1, right)

            return _binary_search(nums, target, left, middle-1)

        return _binary_search(nums, target, 0, len(nums)-1)


if __name__ == "__main__":
    nums = [0, 1, 5, 7, 9, 11, 15, 20, 24]
    search = Search()
    print(search.binary_search(nums, 15))
    print(search.recursive_binary_search(nums, 15))