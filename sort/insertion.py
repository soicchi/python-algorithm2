class Sort:
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
    samples = [random.randint(1, 1000) for _ in range(10)]
    sort = Sort()
    print(sort.insertion_sort(samples))