class Solution(object):
    def quickFind(self, n, edges):
        uf = [i for i in range(n)]
        count = n
        for u, v in edges:
            #if u and v are in the same union
            if uf[u] == uf[v]:
                continue
            g_u, g_v = uf[u], uf[v]
            # make u and v are in the same union
            for i in range(n):
                if uf[i] == g_v:
                    uf[i] = g_u
            count -= 1
        return count

    def quickUnion(self, n, edges):
        uf = [i for i in range(n)]
        self.count = n

        def find(u):
            while u != uf[u]:
                u = uf[u]
            return u
            '''
            if u != uf[u]:
                return find(uf[u])
            return u'''
        def union(u, v):
            p_u = find(u)
            p_v = find(v)
            if p_u == p_v:
                return
            uf[p_u] = p_v
            self.count -= 1

        for u, v in edges:
            union(u, v)
        return self.count

    def quickUnion_byRank(self, n, edges):

        uf = [i for i in range(n)]
        size = [i for i in range(n)]
        self.count = n

        def find(u):
            if u != uf[u]:
                return find(uf[u])
            return u

        def union(u, v):
            p_u = find(u)
            p_v = find(v)
            if p_u == p_v:
                return
            if size[p_u] < size[p_v]:
                uf[p_u] = p_v
                size[p_v] += size[p_u]
            else:
                uf[p_v] = p_u
                size[p_u] += size[p_v]
            self.count -= 1

        for u, v in edges:
            union(u, v)
        return self.count

    def quickUnion_pathCompression(self, n, edges):

        uf = [i for i in range(n)]
        size = [i for i in range(n)]
        self.count = n

        def find(u):
            if uf[u] != uf[uf[u]]:
                uf[u] = find(uf[u])
            return uf[u]

        def union(u, v):
            p_u = find(u)
            p_v = find(v)
            if p_u == p_v:
                return
            if size[p_u] < size[p_v]:
                uf[p_u] = p_v
                size[p_v] += size[p_u]
            else:
                uf[p_v] = p_u
                size[p_u] += size[p_v]
            self.count -= 1

        for u, v in edges:
            union(u, v)
        return self.count

n = 4
e = [[2,3],[1,2],[1,3]]
s =Solution()
print s.quickUnion2(n, e)