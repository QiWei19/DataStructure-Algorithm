import heapq

class ShortestPath:
    def dijkstra(self, graph, s):
        self.dist = {s: 0}
        self.path = {}
        self.pq = [[0, s]]

        while self.pq:
            d, u = heapq.heappop(self.pq)
            if u not in adj:
                continue
            for v in graph[u]:
                self.relax(u, v, graph[u][v])

        print self.dist
        print self.path

        return

    def relax(self, u, v, cost):
        if v not in self.dist:
            self.dist[v] = float("inf")
        if self.dist[v] > self.dist[u] + cost:
            self.dist[v] = self.dist[u] + cost
            self.path[v] = u
            heapq.heappush(self.pq, [self.dist[v], v])



if __name__ == "__main__":
    edges = [
        ["a", "b", 7],
        ["a", "d", 5],
        ["b", "c", 8],
        ["b", "d", 9],
        ["b", "e", 7],
        ["c", "e", 5],
        ["d", "e", 15],
        ["d", "f", 6],
        ["e", "f", 8],
        ["e", "g", 9],
        ["f", "g", 11]
    ]

    adj = {}
    for u, v, c in edges:
        if u not in adj:
            adj[u] = {}
        adj[u][v] = c

    start = "a"
    solution = ShortestPath()
    solution.dijkstra(adj, start)

    start = "b"
    solution = ShortestPath()
    solution.dijkstra(adj, start)