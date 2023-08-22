class TwoStacks:
    def __init__(self, n=100):
        self.size = n
        self.arr = [0] * n
        self.top1 = -1
        self.top2 = n

    def push1(self, x):
        if (self.top1 <= self.top2):
            self.top1 += 1
            self.arr[self.top1] = x
        else:
            return -1
        pass

    def push2(self, x):
        if (self.top1 <= self.top2):
            self.top2 -= 1
            self.arr[self.top2] = x
        else:
            return -1
        pass

    def pop1(self):
        if (self.top1 >= 0):
            popped = self.arr[self.top1]
            self.top1 -= 1
            return popped
        else:
            return -1
        pass

    def pop2(self):
        if (self.top2 < self.size):
            popped = self.arr[self.top2]
            self.top2 += 1
            return popped
        else:
            return -1
        pass


# Driver Code
if __name__ == '__main__':
    T = int(input())
    while T > 0:
        sq = TwoStacks()
        Q = int(input())
        while Q > 0:
            query = list(map(int, input().split()))
            if query[1] == 1:
                if query[0] == 1:
                    sq.push1(query[2])
                elif query[0] == 2:
                    sq.push2(query[2])
            elif query[1] == 2:
                if query[0] == 1:
                    print(sq.pop1(), end=' ')
                elif query[0] == 2:
                    print(sq.pop2(), end=' ')
            Q -= 1
        print()
        T -= 1
