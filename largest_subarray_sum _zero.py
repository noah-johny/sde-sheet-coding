class Solution:
    def maxLen(self, n, arr):
        if n == 0:
            return 0

        cum_sum = max_len = 0
        sum_index_dict = {0: -1}

        for i in range(n):
            cum_sum += arr[i]

            if cum_sum in sum_index_dict:
                max_len = max(max_len, i - sum_index_dict[cum_sum])
            else:
                sum_index_dict[cum_sum] = i

        return max_len


# Driver Code
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n, arr))
