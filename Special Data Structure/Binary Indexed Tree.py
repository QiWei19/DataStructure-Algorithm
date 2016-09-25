class BinaryIndexedTree:
    def __init__(self,a):
        self.a = a
        self.c = [0 for i in range(len(a)+1)]
        for i in range(len(a)):
            self.update(i+1,a[i])
    def lowBit(self,t):
        return t&(-t)
    def update(self,i,x):
        self.a[i] += x
        while i <= len(self.a):
            self.c[i] += x
            i += self.lowBit(i)
    def sum(self,i):
        res = 0
        while i > 0:
            res += self.c[i]
            i -= self.lowBit(i)
        return res


class BinaryIndexedTree_2dimension:
    def __init__(self,a):
        self.a = a
        self.c = [[0 for i in range(len(a[0])+1)] for j in range(len(a)+1)]
        for i in range(len(a)):
            for j in range(len(a[0])):
                self.update2(a[i][j])
    def lowBit(self,t):
        return t&(-t)
    def update2(self,i,j,x):
        self.a[i][j] += x
        temp = j
        while i <= len(self.a):
            while j <= len(self.a[0]):
                self.c[i][j] += x
                j += self.lowBit(j)
            j = temp
            i += self.lowBit(i)
    def sum2(self,i,j):
        res = 0
        temp = j
        while i > 0:
            while j > 0:
                res += self.c[i][j]
                j -= self.lowBit(j)
            j = temp
            i -= self.lowBit(i)
        return res