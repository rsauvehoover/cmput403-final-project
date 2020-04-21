import pytest
from hollow_heap import Element, HollowHeap

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

    a.delete_min()

    assert a.min_key() == 3

    a.delete_min()

    assert a.min_key() == 4

def test_meld():
    a = HollowHeap()
    b = HollowHeap()

    a.insert(4)
    b.insert(3)

    assert a.min_key() == 4
    assert b.min_key() == 3

    a.meld(b.h)

    assert a.min_key() == 3
    assert b.min_key() == 3
    
    a = HollowHeap()
    b = HollowHeap()

    a.insert(4)
    b.insert(3)

    assert a.min_key() == 4
    assert b.min_key() == 3

    b.meld(a.h)

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
