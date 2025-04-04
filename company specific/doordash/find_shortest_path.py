"""
A dasher sometimes travels between cities. To avoid delays, the dasher first checks for the shortest routes. Given a map of the cities and their bidirectional roads represented by a graph of nodes and edges, determine which given roads are along any shortest path. Return an array of strings, one for each road in order, where the value is YES if the road is along a shortest path or NO if it is not.The roads or edges are named using their 1-based index within the input arrays.

Example given a map of g_nodes = 5 nodes, the starting nodes, ending nodes and road lengths are:

Road from/to/weight
1 (1, 2, 1)
2 (2, 3, 1)
3 (3, 4, 1)
4 (4, 5, 1)
5 (5, 1, 3)
6 (1, 3, 2)
7 (5, 3, 1)

Example Input: (5, [1, 2, 3, 4, 5, 1, 5], [
2, 3, 4, 5, 1, 3, 3], [1, 1, 1, 1, 3, 2, 1])
The traveller must travel from city 1 to city g_nodes, so from node 1 to node 5 in this case. The shortest path is 3 units long and there are three paths of that length: 1 → 5, 1 → 2 → 3 → 5, and 1 → 3 → 5. Return an array of strings, one for each road in order, where the value is YES if a road is along a shortest path or NO if it is not. In this case, the resulting array is ['YES', 'YES', 'NO', 'NO', 'YES', 'YES', 'YES']. The third and fourth roads connect nodes (3, 4) and (4, 5) respectively. They are not on a shortest path, i.e. one with a length of 3 in this case.
"""

import collections, heapq


def find_shortest_paths(g_nodes, sources, destinations, weights):
    graph = collections.defaultdict(list)
    weight_between = {}
    for s, d, w in zip(sources, destinations, weights):
        graph[s].append(d)
        graph[d].append(s)
        weight_between[(s, d)] = w
        weight_between[(d, s)] = w

    parents = collections.defaultdict(set)

    dist = collections.defaultdict(lambda: float('inf'))
    dist[1] = 0

    def relaxation(v, u, w):
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            parents[v] = {u}
        elif dist[v] == dist[u] + w:
            parents[v].add(u)

    q = [(0, 1)]
    relaxed = set()
    while q:
        _, node = heapq.heappop(q)

        for nei in graph[node]:
            if nei not in relaxed:
                relaxation(nei, node, weight_between[(nei, node)])
                heapq.heappush(q, (weight_between[(nei, node)], nei))

        relaxed.add(node)


    shortest_edges = set()
    visited = set()
    dfs(g_nodes, parents, visited, shortest_edges)

    ans = []
    for s, d in zip(sources, destinations):
        if (s, d) in shortest_edges or (d, s) in shortest_edges:
            ans.append('YES')
        else:
            ans.append('NO')
    print(parents)
    print(ans)


def dfs(node, parents, visited, shortest_edges):
    if node in visited:
        return
    visited.add(node)
    while parents[node]:
        p = parents[node].pop()
        shortest_edges.add((node, p))
        dfs(p, parents, visited, shortest_edges)


if __name__ == '__main__':
    find_shortest_paths(
        5,
        [1, 2, 3, 4, 5, 1, 5],
        [2, 3, 4, 5, 1, 3, 3],
        [1, 1, 1, 1, 3, 2, 1]
    )