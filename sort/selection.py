class Sort:
    def selection_sort(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        for i in range(len_nums):
            min_index = i
            for j in range(i+1, len_nums):
                if nums[min_index] > nums[j]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]

        return nums


if __name__ == "__main__":
    import random
    samples = [random.randint(1, 1000) for _ in range(10)]
    sort = Sort()
    print(sort.selection_sort(samples))