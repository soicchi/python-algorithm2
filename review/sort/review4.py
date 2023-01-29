class Sort:
    def bubble_sort(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        for i in range(len_nums):
            for j in range(len_nums -i -1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return nums

    def selection_sort(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        for i in range(len_nums):
            min_index = i
            for j in range(i+1, len_nums):
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

if __name__ == "__main__":
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    sort = Sort()
    print(sort.bubble_sort(nums))
    print(sort.selection_sort(nums))
    print(sort.insertion_sort(nums))