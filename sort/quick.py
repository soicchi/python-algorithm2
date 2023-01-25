class Sort:
    def quick_sort(self, nums: list[int]) -> list[int]:
        self._quick_sort(nums, 0, len(nums)-1)

        return nums

    def _quick_sort(self, nums: list[int], low: int , high: int) -> None:
        if low < high:
            partition_index = self._partition(nums, low, high)
            self._quick_sort(nums, low, partition_index-1)
            self._quick_sort(nums, partition_index+1, high)

    def _partition(self, nums: list[int], low: int, high: int) -> int:
        i = low - 1
        pivot = nums[high]
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[high] = nums[high], nums[i+1]

        return i+1


if __name__ == "__main__":
    import random
    samples = [random.randint(1, 1000) for _ in range(10)]
    sort = Sort()
    print(sort.quick_sort(samples))
