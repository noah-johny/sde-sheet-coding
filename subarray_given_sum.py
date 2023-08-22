class Solution:
    def subArraySum(self, arr, n, s):
        total_sum = sum(arr)
        if total_sum < s or s == 0:
            return [-1]
        elif total_sum == s:
            if n == 1:
                return [1]
            else:
                return [1, n]

        left = right = 0
        current_sum = 0

        while right < n:
            current_sum += arr[right]

            while current_sum > s:
                current_sum -= arr[left]
                left += 1

            if current_sum == s:
                return [left + 1, right + 1]

            right += 1

        return [-1]


# Driver Code
def main():
    T = int(input())
    while (T > 0):

        NS = input().strip().split()
        N = int(NS[0])
        S = int(NS[1])

        A = list(map(int, input().split()))
        ob = Solution()
        ans = ob.subArraySum(A, N, S)

        for i in ans:
            print(i, end=" ")

        print()

        T -= 1


if __name__ == "__main__":
    main()
