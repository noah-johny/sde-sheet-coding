class Solution:
    def findSubArrays(self, arr, n):
        if n < 1:
            return 0

        cum_sum_freq = {0: 1}

        cum_sum = 0
        count = 0

        for num in arr:
            cum_sum += num
            if cum_sum in cum_sum_freq:
                count += cum_sum_freq[cum_sum]
                cum_sum_freq[cum_sum] += 1
            else:
                cum_sum_freq[cum_sum] = 1

        return count


# Driver Code
if __name__ == '__main__':
    t = int(input())
    for tc in range(t):

        N = int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ob = Solution()
        print(ob.findSubArrays(A, N))
