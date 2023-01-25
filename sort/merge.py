class MergeSort:
    def sort(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        if len_nums <= 1:
            return nums

        center = len_nums // 2
        left = nums[:center]
        right = nums[center:]

        self.sort(left)
        self.sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
                k += 1
                continue

            nums[k] = right[j]
            j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

        return nums


if __name__ == "__main__":
    import random
    samples = [random.randint(1, 1000) for _ in range(10)]
    merge_sort = MergeSort()
    print(merge_sort.sort(samples))
