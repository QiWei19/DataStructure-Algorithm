class Solution3(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        used = set([])
        alpha = "qwertyuiopasdfghjklzxcvbnm"
        begin, end = set([beginWord]), set([endWord])
        parent_b, parent_e = {beginWord: []}, {endWord: []}
        meet = set([])
        while begin and end:
            if len(begin) > len(end):
                begin, end = end, begin
                parent_b, parent_e = parent_e, parent_b
            next = set([])
            temp = {}
            for w in begin:
                for i in range(len(w)):
                    for c in alpha:
                        new = w[:i]+c+w[i+1:]
                        if new in wordlist and new not in parent_b and new != w:
                            if new not in temp:
                                temp[new] = set([])
                            temp[new].add(w)
                            if new in parent_e:
                                meet.add(new)
                            else:
                                next.add(new)
            begin = next
            parent_b.update(temp)
            if meet:
                break
        if beginWord in parent_e:
            parent_b, parent_e = parent_e, parent_b
        return self.buildPath(parent_b, parent_e, meet)

    def buildPath(self, begin, end, meet):
        res = []
        for node in meet:
            path_begin = self.dfs(node, begin, [], [])
            path_end = self.dfs(node, end, [], [])
            for p1 in path_begin:
                for p2 in path_end:
                    res.append(p1[::-1]+[node]+p2)
        return res
        
    def dfs(self, root, parent, cur, res):
        if parent[root] == []:
            res.append(cur)
            return res
        for p in parent[root]:
            self.dfs(p, parent, cur+[p], res)
        return res

s = Solution3()
b = "red"
e = "tax"
l = ["ted","tex","red","tax","tad","den","rex","pee"]
b = "hit"
e = "cog"
l = ["hot","cog","dot","dog","hit","lot","log"]

print s.findLadders(b,e,l)
