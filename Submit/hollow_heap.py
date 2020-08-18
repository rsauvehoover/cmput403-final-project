"""
Implementation based on the Hollow Heap based on paper by Hansen et al. https://arxiv.org/abs/1510.06535
"""

class HollowHeap:
    def __init__(self):
        # Full roots 
        self.A = {}
        # our root node
        self.h = None
        self.max_rank = 0

    def find_min(self):
        """find item with minimum key in h
        :return: item with min key, null if h is empty
        """
        if self.h is None:
            return None
        return self.h.item

    def insert(self, k, e = None):
        """
        Insert item e with key k. e must not be in h
        :return: the heap with e added"""
        if e is None:
            e = Element()
        self.h = HollowHeap.meld(_HollowHeapNode(e, k), self.h)
        return self.h

    def delete_min(self):
        """
        delete the mimimum item of the heap
        :return: the key of the deleted item, None if the heap is empty
        """
        val = self.min_key()
        if val is not None:
            self.delete(self.h.item)
        return val

    def meld(h, g):
        """
        melds g into self.h, where g and self.h have distinct keys
        """
        if g is None: 
            return h
        if h is None: 
            return g
        return _HollowHeapNode._link(h, g)

    def decrease_key(self, e, k):
        """
        changes the key of element e to k, if e originally has a key larger than k
        """
        u = e.node
        if u == self.h:
            u.key = k
            return
        v = _HollowHeapNode(e, k)
        u.item = None
        if u.rank > 2:
            v.rank = u.rank - 2
        v.child = u
        u.ep = v
        self.h = _HollowHeapNode._link(self.h, v)

    def delete(self, e):
        """
        delete e from heap h
        """
        # set the element to be hollow
        e.node.item = None
        e.node = None

        # we need to reset A and max_rank
        self.max_rank = 0
        self.A = {}

        # if we're deleting something other than our min, then we don't need
        # to do anything else
        if self.h is not None and self.h.item is not None:
            return

        while self.h is not None:
            w = self.h.child
            v = self.h
            self.h = self.h.next
            
            while w is not None:
                u = w
                w = w.next
                if u.item is None:
                    if u.ep is None:
                        u.next = self.h
                        self.h = u
                    else:
                        if u.ep == v:
                            w = None
                        else:
                            u.next = None
                        u.ep = None
                else:
                    self._do_ranked_links(u)
        self._do_unranked_links()
        #  we need to reset the next on the root
        if self.h is not None:
            self.h.next = None

    
    def _do_ranked_links(self, u):
        """
        link nodes based on rankings
        """
        while u.rank in self.A and self.A[u.rank] is not None:
            u = _HollowHeapNode._link(u, self.A[u.rank])
            self.A[u.rank] = None
            u.rank += 1
        self.A[u.rank] = u
        self.max_rank = max(self.max_rank, u.rank)

    def _do_unranked_links(self):
        for i in range(self.max_rank + 1):
            if i in self.A and self.A[i] is not None:
                if self.h is None:
                    self.h = self.A[i]
                else:
                    self.h = _HollowHeapNode._link(self.h, self.A[i])
                self.A[i] = None

    def min_key(self):
        """
        returns the integer value of the minimum key in the heap
        :return: key, or None if the heap is empty
        """
        m = self.find_min()
        if m is None:
            return None
        else:
            return m.node.key


class _HollowHeapNode:
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

    def _add_child(v, w):
        """
        Auxillary function,
        adds v as a child of w
        """
        v.next = w.child
        w.child = v

    def _link(v, w):
        """
        Auxillary function,
        makes the node with the larger key a child of the smaller
        :return: the smaller node
        """
        if v.key >= w.key:
            _HollowHeapNode._add_child(v, w)
            return w
        else:
            _HollowHeapNode._add_child(w, v)
            return v

class Element:
    """
    Element data structure, contains only a reference to the node containing it
    """
    def __init__(self, data=None):
        self.node = None
        # whatever data you want to store in it, should be a pointer to some object
        self.data = data
