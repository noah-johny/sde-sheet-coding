class Solution:
    def calculateSpan(self, a, n):
        if n < 1:
            return 0

        span = [1]
        stack = [(a[0], 0)]

        for i in range(1, n):
            while stack and a[i] >= stack[-1][0]:
                stack.pop()

            if not stack:
                span.append(i + 1)
            else:
                span.append(i - stack[-1][1])

            stack.append((a[i], i))

        return span


# Driver Code
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        ans = obj.calculateSpan(a, n)
        for i in range(n):
            print(ans[i], end=" ")
        print()
