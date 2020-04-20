"""
Implementation based on the Hollow Heap paper by Hansen et al. https://arxiv.org/abs/1510.06535
"""

class HollowHeap:
    def make_heap():
        """
        :return: empty heap
        """
        return None

    def find_min(h):
        """find item with minimum key in h
        :return: item with min key, null if h is empty
        """
        if h is None:
            return None
        return h.item

    def insert(e,k,h):
        """
        Insert item e with key k. e must not be in h
        :return: a heap containing e"""
        return HollowHeap.meld(HollowHeapNode(e, k), h)

    def delete_min(h):
        """
        delete the mimimum item of heap h
        :return: heap without min key item"""
        return delete(h.item, h)

    def meld(h1, h2):
        """
        union of two item-disjoint heaps h1, h2
        :return: the heap containing all items of h1 and h2"""
        if h1 is None: 
            return h2
        if h2 is None: 
            return h1
        return HollowHeap.link(h1,h2)

    def decrease_key(e, k, h):
        """
        """
        u = e.node
        if u == h:
            u.key = k
            return h
        v = HollowHeapNode(e, k)
        u.item = None


        pass

    def delete(e, h):
        """
        delete e from heap h
        :return: heap resulting from the deletion"""
        pass

    def add_child(v, w):
        v.next = w.child
        w.child = v

class HollowHeapNode:
    """
    The node data structure
    """
    def __init__(self, e, k):
        self.item = e
        self.key = k
        self.child = None
        self.next = None
        self.ep = None
        self.rank = 0
        e.node = self

class Element:
    """
    Element data structure, contains only a reference to the node containing it
    """
    def __init__(self):
        self.node = None
