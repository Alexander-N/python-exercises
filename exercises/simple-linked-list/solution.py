class Node(object):
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedIterator(object):
    def __init__(self, linked_list):
        self.current = linked_list._head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.value()
        self.current = self.current.next()
        return value

    def next(self):
        return self.__next__()


class LinkedList(object):
    def __init__(self, values=[]):
        self._head = None
        self._len = 0
        [self.push(v) for v in values]

    def __iter__(self):
        return LinkedIterator(self)

    def __len__(self):
        return self._len

    def head(self):
        if self._head is None:
            raise EmptyListException("The list is empty")
        return self._head

    def push(self, value):
        newNode = Node(value)
        newNode._next = self._head
        self._head = newNode
        self._len += 1

    def pop(self):
        if self._head is None:
            raise EmptyListException("The list is empty")
        self._len -= 1
        ret = self._head.value()
        self._head = self._head.next()
        return ret

    def reversed(self):
        return LinkedList(self)


class EmptyListException(Exception):
    pass
