__author__ = 'wq'
import math
class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)
        if self.size:
            #the height of segment tree
            h = int(math.ceil(math.log(self.size, 2)))
            #the maximum size of segment tree
            #it includes the value itself, which is the leaf node.
            # so it is (h+1),not h
            maxSize = 2 ** (h+1) - 1
            self.tree = [0] * maxSize
            self.initSegmentTree(0, self.size-1, 0)
        else:
            self.tree = []
        print self.tree

    def initSegmentTree(self, start, end, i):
        #when the node contatins only one element
        if start == end:
            self.tree[i] = self.nums[start]
        #otherwise, get the values left and right children
        else:
            mid = (start + end)/2
            self.tree[i] = self.initSegmentTree(start, mid, 2*i+1)
            self.tree[i] += self.initSegmentTree(mid+1, end, 2*i+2)
        return self.tree[i]

    def update(self,val,i):
        #if i is invalid
        if i < 0 or i > self.size:
            return
        #get the difference
        diff = val - self.nums[i]
        self.nums[i] = val
        self.__updateSegmentTree(0, self.size-1, i, diff, 0)
        print self.tree

    def __updateSegmentTree(self, start, end, i, diff, tree_index):
        #if the i is not in range [start, end]
        if i < start or i > end:
            return
        self.tree[tree_index] += diff
        if start != end:
            mid = (start + end)/2
            #although we update both left and right here
            #actually, only one of them really updates
            #the other will makes i not in the valid range
            self.__updateSegmentTree(start, mid, i, diff, 2*tree_index+1)
            self.__updateSegmentTree(mid+1, end, i, diff, 2*tree_index+2 )

    def sumRange(self, i, j):
        #if input i, j are invalid
        if i < 0 or i >= self.size or j < 0 or j >= self.size:
            return 0
        return self.__sumRangeSegmentTree(0, self.size-1, i, j, 0)

    def __sumRangeSegmentTree(self,start, end, i, j, tree_index):
        #if the query range is within current node range
        #return the value of current node
        if i <= start and j >= end:
            return self.tree[tree_index]
        #if the query range is not in current node range at all
        if end < i or start > j:
            return 0
        #if the query range and the current node range has some overlaps
        mid = (start + end)/2
        sum = self.__sumRangeSegmentTree(start, mid, i, j, 2*tree_index+1)
        sum += self.__sumRangeSegmentTree(mid+1, end, i, j, 2*tree_index+2)
        return sum


num = [1,2,3,4,5]
s = SegmentTree(num)
s.update(2, 0)
print s.sumRange(0, 3)