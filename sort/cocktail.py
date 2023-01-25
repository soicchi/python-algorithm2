class Sort:
    def cocktail_sort(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        swapped = True
        start = 0
        end = len_nums - 1
        while swapped:
            swapped = False
            for i in range(start, end):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    swapped = True

            swapped = False
            end = end - 1

            for i in range(end-1, start-1, -1):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    swapped = True

            start = start + 1

        return nums


if __name__ == "__main__":
    import random
    sample_list = [random.randint(1, 1000) for _ in range(10)]
    sort = Sort()
    print(sort.cocktail_sort(sample_list))
