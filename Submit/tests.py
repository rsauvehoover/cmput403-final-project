import pytest
from hollow_heap import Element, HollowHeap
import random

def test_insert():
    a = HollowHeap()
    # h should be null when intialized
    assert a.h is None

    a.insert(3)
    # item of h should exist now, and be equal to our newly added key
    assert a.h.item is not None
    assert a.h.item.node.key == 3

    a.insert(4)
    # inserting a larger key should keep h.item the same
    assert a.h.item.node.key == 3

    a.insert(2)
    # inserting a smaller key should update h.item
    assert a.h.item.node.key == 2


    # run the same tests passing in en Element()
    a = HollowHeap()
    # h should be null when intialized
    assert a.h is None

    a.insert(3, Element())
    # item of h should exist now, and be equal to our newly added key
    assert a.h.item is not None
    assert a.h.item.node.key == 3

    el = Element()
    a.insert(4, el)
    # inserting a larger key should keep h.item the same
    assert a.h.item.node.key == 3

    a.insert(2, Element)
    # inserting a smaller key should update h.item
    assert a.h.item.node.key == 2

def test_find_min_key():
    a = HollowHeap()

    a.insert(3)
    assert a.min_key() == 3

    a.insert(4)
    assert a.min_key() == 3

    a.insert(2)
    assert a.min_key() == 2

def test_delete_min():
    a = HollowHeap()

    a.insert(3)
    a.insert(4)
    a.insert(2)

    assert a.min_key() == 2
    assert a.delete_min() == 2

    assert a.min_key() == 3
    assert a.delete_min() == 3

    assert a.min_key() == 4
    assert a.delete_min() == 4

    assert a.min_key() is None
    assert a.delete_min() is None

    assert a.min_key() is None

def test_delete():
    a = HollowHeap()

    e = Element()
    a.insert(3, e)
    a.insert(2)

    a.delete(e)
    assert a.min_key() == 2

    a.delete_min()

    assert a.min_key() is None

def test_delete_multiple():
    a = HollowHeap()

    L = list(range(100))
    for i in L:
        a.insert(i)

    S = [a.delete_min() for _ in range(100)]

    assert S == list(sorted(L))

def test_sort_list_reversed():
    a = HollowHeap()

    L = list(reversed(range(100)))
    for i in L:
        a.insert(i)

    S = [a.delete_min() for _ in range(100)]

    assert S == list(sorted(L))

def test_sort_list_random():
    a = HollowHeap()

    L = list(range(100))
    random.shuffle(L)
    for i in L:
        a.insert(i)

    S = [a.delete_min() for _ in range(100)]

    assert S == list(sorted(L))

def test_meld():
    a = HollowHeap()
    b = HollowHeap()

    a.insert(4)
    b.insert(3)

    assert a.min_key() == 4
    assert b.min_key() == 3

    a.h = HollowHeap.meld(b.h, a.h)

    assert a.min_key() == 3
    assert b.min_key() == 3
    
    a = HollowHeap()
    b = HollowHeap()

    a.insert(4)
    b.insert(3)

    assert a.min_key() == 4
    assert b.min_key() == 3

    b.h = HollowHeap.meld(b.h, a.h)

    assert a.min_key() == 4
    assert b.min_key() == 3

def test_decrease_key():
    a = HollowHeap()

    a.insert(4)

    assert a.min_key() == 4

    a.decrease_key(a.find_min(), 3)

    assert a.min_key() == 3

    a.decrease_key(a.find_min(), 0)

    assert a.min_key() == 0

def test_element_data():
    a = HollowHeap()

    e = Element([1,2,3])

    a.insert(3, e)

    assert a.find_min().data == [1,2,3]

    a.insert(2)

    assert a.find_min().data != [1,2,3]

    a.delete_min()

    assert a.find_min().data == [1,2,3]
