from hollow_heap import Element, HollowHeap
import random
import copy

import time

import heapq

LENGTH = 100000

def heapsort_hollow(A):
    h = HollowHeap()
    for v in A:
        h.insert(v)
    return [h.delete_min() for _ in range(LENGTH)]

def heapsort_heapq(A):
    h = []
    for v in A:
        heapq.heappush(h, v)
    return [heapq.heappop(h) for _ in range(LENGTH)]

def time_sort(function, L):
    t1 = time.time()
    function(L)
    t2 = time.time()
    return t2-t1

print("TESTING HEAPSORT on list of length {}".format(LENGTH))

L = list(range(LENGTH))

print('~'*60)
print("Reverse order")

L_reversed = list(reversed(L))

print("Hollow heap completed in {}s".format(time_sort(heapsort_hollow, L_reversed)))
print("heapq completed in {}s".format(time_sort(heapsort_heapq, L_reversed)))
print("builtin sort completed in {}s".format(time_sort(sorted, L_reversed)))

print('~'*60)
print("Random order")

L_randomized = copy.copy(L)
random.shuffle(L_randomized)

print("Hollow heap completed in {}s".format(time_sort(heapsort_hollow, L_randomized)))
print("heapq completed in {}s".format(time_sort(heapsort_heapq, L_randomized)))
print("builtin sort completed in {}s".format(time_sort(sorted, L_randomized)))


print('~'*60)
print("Already Sorted")

print("Hollow heap completed in {}s".format(time_sort(heapsort_hollow, L)))
print("heapq completed in {}s".format(time_sort(heapsort_heapq, L)))
print("builtin sort completed in {}s".format(time_sort(sorted, L)))
