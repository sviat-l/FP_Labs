"""
Lab 11 task1
Miltiset implemented as a linked list
"""

class Node:
    """
    Node class for linked list
    """

    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next

class Multiset:

    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        __init__: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None

    def empty(self):
        """
        Checks emptiness of Multiset.
        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """
        return self._head == None

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current != None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.next = rest

    def delete(self, value):
        """

        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next

    def remove_all(self):
        """
        remove all links and save data values in list
        get data from head to tail
        """
        result = []
        while not self.empty():
            result.append(self._head.item)
            self._head = self._head.next
        return result


    def split_half(self):
        """
        split linked list into two multisets with equel length,
        If initial number of elements is odd add, one element to first multiset
        If there are less then 2 elements return None
        """
        # len < 2
        if self._head is None or self._head.next is None:
            return None
        # init first and second heads
        first = self._head
        second = self._head.next
        # move second 2 steps forward and first one step
        while second is not None and second.next is not None:
            second = second.next
            first, second = first.next, second.next
        # create second multiset
        second_mls = Multiset()
        second_mls._head = first.next
        # delete link between first and second part
        first.next = None
        return self, second_mls



    def extend(self, other):
        """
        extend one multiset with another. Return head of the
        multiset which contains all elements of both sets
        """
        tmp = other._head
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = self._head
        # if also safe inplace
        self._head = other._head
        return other
