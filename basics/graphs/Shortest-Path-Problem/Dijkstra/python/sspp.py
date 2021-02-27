# using Dijkstra's algorithm
import heapq
from collections import defaultdict

'''
6 7
A B 4
A C 2 
B C 5 
B D 10
C E 3
D F 11
E D 4
A D
'''

def get_shortest_path(graph, src, dest):
    h = []
    # keep a track record of vertices with the cost
    # heappop will return vertex with least cost
    # greedy SRC -> MIN -> MIN -> DEST

    heapq.heappush(h, (0, src))
    while len(h) != 0:
        current_cost, current_vertex = heapq.heappop(h)
        if current_vertex == dest:
            print("Path Exist {} to {} with cost {}".format(
                src, dest, current_cost))
            break
        for neighbor, neighbor_cost in graph[current_vertex]:
            heapq.heappush(h, (current_cost + neighbor_cost, neighbor))


graph = defaultdict(list)
v, e = map(int, input().split())

for i in range(e):
    u, v, w = map(str, input().split())
    graph[u].append((v, int(w)))
src, dest = map(str, input().split())
get_shortest_path(graph, src, dest)
