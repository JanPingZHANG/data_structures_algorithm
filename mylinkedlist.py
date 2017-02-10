#!/usr/bin/env python
# encoding: utf-8
class Node(object):
    def __init__(self,value=None):
        self.value = value
        self.behind =None
    def __del__(self):
        print('a node was del, %s '%self.value)


class MyLinkedlist(object):
    def __init__(self):
        self.count = 0
        self.head = Node()

    def append(self,elem):
        node = Node(elem)
        end = self.head
        while end.behind is not None:
            end = end.behind
        end.behind = node
        self.count = self.count+1

    def insert(self,elem,index):
        if index < 0:
            raise IndexError('the index must be greater than or equal to 0')
        node = Node(elem)
        find = self.head
        for _ in range(index):
            find = find.behind
            if find is None:
                raise IndexError('the index is out of range')
        node.behind = find.behind
        find.behind = node
        self.count = self.count + 1

    def clear(self):
        self.count = 0
        self.head.behind = None

    def pop(self):
        if self.count == 0:
            raise IndexError('the list is empty')
        find = self.head
        for _ in range(self.count-1):
            find = find.behind
        node = find.behind
        find.behind = None
        return node.value

    def get(self,index):
        if index > self.count-1:
            raise IndexError('the index is out of range')
        find = self.head
        for _ in range(index+1):
            find = find.behind
        return find.value

    def remove(self,index):
        if index > self.count-1:
            raise IndexError('the index is out of range')
        find = self.head
        for _ in range(index):
            find = find.behind
        node = find.behind
        find.behind = node.behind
        return node.value

    def index(self,elem):
        pass
    def reverse(self):
        pass
    def sort(self):
        pass
    def extend(self,otherlist):
        pass

mylist =MyLinkedlist()
for i in range(10):
    mylist.append(i)
for i in range(10):
    print(mylist.get(i))
mylist.insert(-1,0)
mylist.insert('num',5)
for i in range(mylist.count):
    print(mylist.get(i))
print(mylist.pop())
print('remove 3: %s'%mylist.remove(3))
mylist.clear()
print('mylist have been clear')
del mylist
print('mylist have been del')
