class Solution:
    def minSwaps(self, nums):
        sorted_nums = sorted(nums)
        swaps = 0

        if len(nums) <= 1:
            return 0

        index_mapping = {num: index for index, num in enumerate(nums)}

        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                value = nums[i]
                swap_index = index_mapping[sorted_nums[i]]
                nums[i] = sorted_nums[i]
                nums[swap_index] = value
                index_mapping[value] = swap_index
                swaps += 1

        return swaps


# Driver Code
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        nums = list(map(int, input().split()))
        obj = Solution()
        ans = obj.minSwaps(nums)
        print(ans)
