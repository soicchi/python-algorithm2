class Sort:
    def bubble_sort(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        for i in range(len_nums):
            for j in range(len_nums - 1 - i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return nums

    def selection_sort(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        for i in range(len_nums-1):
            min_index = i
            for j in range(i, len_nums):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]

        return nums

    def insertion_sort(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        for i in range(1, len_nums):
            temp = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > temp:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = temp

        return nums

    def quick_sort(self, nums: list[int]) -> list[int]:
        def _quick_sort(nums: list[int], low: int, high: int) -> None:
            if low < high:
                partition_index = self._partition(nums, low, high)
                _quick_sort(nums, low, partition_index-1)
                _quick_sort(nums, partition_index+1, high)

    def _partition(self, nums: list[int], low: int, high: int) -> int:
        i = low - i
        pivot = nums[high]
        for j in range(low, high):
            if nums[j] < nums[pivot]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1] = pivot

        return i+1


if __name__ == "__main__":
    import random
    nums = [random.randint(1, 1000) for _ in range(10)]
    sort = Sort()
    print(sort.bubble_sort(nums))
    print(sort.selection_sort(nums))
    print(sort.insertion_sort(nums))
    print(sort.quick_sort(nums))