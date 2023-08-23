class Solution:
    def countOccurence(self, arr, n, k):
        count_dict = {}
        visited = []
        count = 0

        for number in arr:
            if (number in count_dict) and (number not in visited):
                if ((count_dict[number] + 1) > (n/k)):
                    count += 1
                    visited.append(number)
                else:
                    count_dict[number] += 1
            elif (number not in count_dict):
                count_dict[number] = 1
            else:
                continue

        return count


# Driver Code
def main():
    T = int(input())
    while (T > 0):

        N = int(input())

        A = list(map(int, input().split()))

        K = int(input())

        print(Solution().countOccurence(A, N, K))

        T -= 1


if __name__ == "__main__":
    main()
