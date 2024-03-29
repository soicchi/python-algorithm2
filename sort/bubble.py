class Sort:
    def bubble_sort(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        for i in range(len_nums):
            for j in range(len_nums - 1 - i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return nums


if __name__ == "__main__":
    import random
    sample_list = [random.randint(1, 1000) for _ in range(10)]
    sort = Sort()
    print(sort.bubble_sort(sample_list))
