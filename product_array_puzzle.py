class Solution:
    def productExceptSelf(self, nums, n):
        product = 1
        non_zero_product = 1
        zeroes = 0
        product_array = []

        for i in range(0, n):
            if (nums[i] != 0):
                non_zero_product *= nums[i]
            elif (nums[i] == 0):
                zeroes += 1
                product = 0
            elif (product == 0):
                continue
            else:
                product *= nums[i]

        for i in nums:
            if (product == 0):
                if (zeroes > 1):
                    product_array.append(0)
                elif (i != 0 and zeroes == 1):
                    product_array.append(0)
                elif (i == 0 and zeroes == 1):
                    product_array.append(non_zero_product)
            else:
                product_array.append(non_zero_product//i)

        return product_array


# Driver Code
if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr, n)
        print(*ans)
