from hollow_heap import Element, HollowHeap
import heapq
import random
import time
from graph import WeightedGraph

def dijkstra_hollow(G, start, target):
    dist = {}
    prev = {}

    seen = {}

    Q = HollowHeap()
    
    dist[start] = 0
    for v in G.vertices():
        if v != start:
            dist[v] = float('infinity')
            prev[v] = None

    seen[start] = Element(start)
    Q.insert(dist[start], seen[start])

    while Q.min_key() is not None:
        u = Q.find_min().data
        Q.delete_min()

        for v in G.neighbours(u):
            alt = dist[u] + G.get_weight(u, v)
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                if v in seen:
                    Q.decrease_key(seen[v], alt)
                else:
                    seen[v] = Element(v)
                    Q.insert(dist[v], seen[v])

    return dist, prev

def dijkstra_queue(G, start, target):
    dist = {}
    prev = {}

    Q = []

    dist[start] = 0

    for v in G.vertices():
        if v != start:
            dist[v] = float('infinity')
            prev[v] = None


    heapq.heappush(Q, (dist[start], start))

    while Q:
        u = heapq.heappop(Q)[1]

        for v in G.neighbours(u):
            alt = dist[u] + G.get_weight(u, v)
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(Q, (dist[v], v))

    return dist, prev

def time_dijkstras(func, G, start, target):
    t1 = time.time()
    s = func(G, start, target)
    t2 = time.time()
    return (t2 - t1), s


NUM_NODES = 1000000
start = random.randint(1, NUM_NODES)
target = random.randint(1, NUM_NODES)
max_weight = 100


print("Graph Tests")
print()
print("~"*60)
print()
print("Testing path with {} nodes".format(NUM_NODES))

G = WeightedGraph()

for i in range(NUM_NODES):
    G.add_edge(i, i+1, random.randint(1, max_weight))

print("Finding shortest path from start={} to target={}...".format(start, target))
timeh, dh = time_dijkstras(dijkstra_hollow,G, start, target)
timeq, dq = time_dijkstras(dijkstra_queue, G, start, target)

assert dh == dq
print("Hollow heap implementation took {}s".format(timeh))
print("heapq implementation took {}s".format(timeq))

print()
print("~"*60)
print()
print("Testing random graph with {} nodes".format(NUM_NODES))

G = WeightedGraph()

for i in range(NUM_NODES):
    G.add_edge(i, random.randint(0, NUM_NODES - 1), random.randint(1, max_weight))

print("Finding shortest path from start={} to target={}...".format(start, target))
timeh, dh = time_dijkstras(dijkstra_hollow,G, start, target)
timeq, dq = time_dijkstras(dijkstra_queue, G, start, target)

assert dh == dq
print("Hollow heap implementation took {}s".format(timeh))
print("heapq implementation took {}s".format(timeq))

print()
print("~"*60)
print()
# graph density
p = 0.5
# we have to decrease this otherwise it becomes really slow to generate
NUM_NODES = 2000
print("Testing random dense-ish graph with p={} and {} nodes".format(p, NUM_NODES))

start = random.randint(1, NUM_NODES)
target = random.randint(1, NUM_NODES)

G = WeightedGraph()

print("Generating graph...")
# generated with erdos-renyi model
for i in range(NUM_NODES):
    for j in range(NUM_NODES):
        if random.random() >= p:
            G.add_edge(i, j, random.randint(1, max_weight))

print("Finding shortest path from start={} to target={}...".format(start, target))
timeh, dh = time_dijkstras(dijkstra_hollow,G, start, target)
print("Hollow heap implementation took {}s".format(timeh))
timeq, dq = time_dijkstras(dijkstra_queue, G, start, target)
print("heapq implementation took {}s".format(timeq))

assert dh[0][target], dq[0][target]

print()
print("~"*60)
print()
# graph density
p = 0.9
NUM_NODES = 9000
print("Testing random dense-ish graph with p={} and {} nodes".format(p, NUM_NODES))

start = random.randint(1, NUM_NODES)
target = random.randint(1, NUM_NODES)

G = WeightedGraph()

print("Generating graph...")
# generated with erdos-renyi model
for i in range(NUM_NODES):
    for j in range(NUM_NODES):
        if random.random() >= p:
            G.add_edge(i, j, random.randint(1, max_weight))

print("Finding shortest path from start={} to target={}...".format(start, target))
timeh, dh = time_dijkstras(dijkstra_hollow,G, start, target)
print("Hollow heap implementation took {}s".format(timeh))
timeq, dq = time_dijkstras(dijkstra_queue, G, start, target)
print("heapq implementation took {}s".format(timeq))

assert dh[0][target], dq[0][target]
