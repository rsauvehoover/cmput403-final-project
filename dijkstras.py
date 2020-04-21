from heapq import heappush, heappop
from hollow_heap import Element, HollowHeap

"""
  R. Frederic Sauve-Hoover
  1455888

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  Code archive dijkstra's implementation

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""

from collections import defaultdict
import heapq

graph = defaultdict(lambda: {})

dist = {v: float('infinity') for v in graph.keys()}
dist[0] = 0

q = [(0, 0, [(0, 0)])]
while q:
    curr_d, curr_v, path = heapq.heappop(q)

    if curr_d > dist[curr_v]:
        continue

    if curr_v == p - 1:
        heapq.heappush(q, (curr_d, curr_v, path))
        break

    for neighbour, weight in graph[curr_v].items():
        total_w = curr_d + weight[0]
        
        # our relaxation condition
        # consider a path if it's better than or equal to any we've already seen
        if total_w <= dist[neighbour]:
            dist[neighbour] = total_w
            heapq.heappush(q, (total_w, neighbour, path + [(curr_v, neighbour)]))

# keep a set of edges we use (to avoid double counting edges that
# appear in multiple shortest paths)
paths_used = set() 
for path in filter(lambda x: x[0] == dist[p-1], q):
    [paths_used.add(node) for node in path[2]]

# remove the 0,0 transition
paths_used.remove((0,0))

# sum up the total length of our unique edges 
total_length = 0
for path in paths_used:
    length = graph[path[0]][path[1]]
    total_length += length[0] * length[1]

print(total_length * 2)


