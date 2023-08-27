class Solution:
    def mergeKArrays(self, arr, K):
        list_arr = []

        for i in range(K):
            list_arr.extend(arr[i])

        list_arr.sort()

        return list_arr


# Driver Code
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        numbers = [[0 for _ in range(n)] for _ in range(n)]
        line = input().strip().split()
        for i in range(n):
            for j in range(n):
                numbers[i][j] = int(line[i*n+j])
        ob = Solution()
        merged_list = ob.mergeKArrays(numbers, n)
        for i in merged_list:
            print(i, end=' ')
        print()
