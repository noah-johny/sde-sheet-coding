class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        arr1_index = arr2_index = 0
        arr = []

        for i in range(n+m):
            if arr1_index >= n or n <= 0:
                arr.append(arr2[arr2_index])
                arr2_index += 1

            elif arr2_index >= m or m <= 0:
                arr.append(arr1[arr1_index])
                arr1_index += 1

            else:
                if arr1[arr1_index] < arr2[arr2_index]:
                    arr.append(arr1[arr1_index])
                    arr1_index += 1
                else:
                    arr.append(arr2[arr2_index])
                    arr2_index += 1

        return arr[k-1]


# Driver Code
def main():

    T = int(input())

    while (T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()
