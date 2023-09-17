class Solution:
    def findMaxLen(ob, S):
        stk = []
        result = 0
        start = 0

        for i in range(len(S)):
            if S[i] == "(":
                stk.append(i)
            else:
                if stk != []:
                    stk.pop()
                else:
                    start = i+1
                    continue

                if stk != []:
                    result = max(result, i - stk[-1])
                else:
                    result = max(result, (i+1) - start)

        return result


# Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.findMaxLen(S))
