class Solution:
    def max_of_subarrays(self, arr, n, k):
        if n < 1 or k <= 0:
            return []

        result = []
        max_val = max(arr[:k])
        result.append(max_val)

        for i in range(1, n - k + 1):
            if arr[i - 1] == max_val:
                max_val = max(arr[i:i + k])
            elif arr[i + k - 1] > max_val:
                max_val = arr[i + k - 1]

            result.append(max_val)

        return result


# Driver Code
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, k = map(int, input().strip().split())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.max_of_subarrays(arr, n, k)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
