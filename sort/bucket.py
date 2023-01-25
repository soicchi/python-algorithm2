class Sort:
    def _insertion_sort(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        for i in range(1, len_nums):
            temp = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > temp:
                nums[j+1] = nums[j]
                j -= 1

            nums[j+1] = temp

        return nums

    def bucket_sort(self, nums: list[int]) -> list[int]:
        max_num = max(nums)
        len_nums = len(nums)
        size = max_num // len_nums

        buckets = [[] for _ in range(size)]
        for num in nums:
            i = num // size
            if i != size:
                buckets[i].append(num)
            else:
                buckets[size-1].append(num)

        for i in range(size):
            self._insertion_sort(buckets[i])

        result = []
        for i in range(size):
            result += buckets[i]

        return result


if __name__ == "__main__":
    import random
    samples = [random.randint(1, 1000) for _ in range(10)]
    sort = Sort()
    print(sort.bucket_sort(samples))
