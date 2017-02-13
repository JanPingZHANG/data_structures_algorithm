#!/usr/bin/env python
# encoding: utf-8
ALLOW_IMBALANCE = 2

class Node(object):
    def __init__(self,element=None,left=None,right=None,height=0):
        self.element = element
        self.left = left
        self.right = right
        self.height = height

class AvlTree(object):
    def __init__(self):
        self.root = None

    def _insert(self,ele,node):
        if node is None:
            return Node(ele)
        if ele > node.element:
            self.right = self._insert(ele,node.right)
        elif ele < node.element:
            self.left = self._insert(ele,node.left)
        self._balance(node)
        return node
    def insert(self,ele):
        self.root = self._insert(ele,self.root)

    def _remove(self,ele,node):
        if node is None:
            raise ValueError('the element not found')
        if ele == node.element:
            if node.left is None and node.right is None:
                return None
            else:
                if node.right is None:
                    node.element = self._findMax(node.left).element
                    node.left = self._remove(node.element,node.left)
                else:
                    node.element = self._findMin(node.right).element
                    node.right = self._remove(node.element,node.right)

        elif ele > node.element:
            node.right = self._remove(ele,node.right)
        elif ele < node.element:
            node.left = self._remove(ele,node.left)
        node = self._blance(node)
        return node
    def remove(self,ele):
        self.root = self._remove(ele,self.root)

    def _findMin(self,node):
        if node.left is not None:
            return self._findMin(node.left)
        return node

    def _findMax(self,node):
        if node.right is not None:
            return self._findMax(node.right)
        return node

    def _height(self,node):
        if node is None:
            return -1
        return node.height

    def _balance(self,node):
        if self._height(node.left) - self._height(node.right) > ALLOW_IMBALANCE:
            if self._height(node.left.left) >= self._height(node.left.right):
                node = self._rotatewithleftchild(node)
            else:
                node = self._doublerotateleft(node)
        elif self._height(node.right) - self._height(node.left) > ALLOW_IMBALANCE:
            if self._height(node.right.right) >= self._height(node.right.left):
                node = self._rotatewithrightchild(node)
            else:
                node = self._doublerotateright(node)
        node.height = max(self._height(node.left),self._height(node.right)) + 1
        return node

    def _rotatewithleftchild(self,node):
        left = node.left
        node.left = left.right
        left.right = node
        return left

    def _rotatewithrightchild(self,node):
        right = node.right
        node.right = right.left
        right.left = node
        return right

    def _doublerotateleft(self,node):
        node.left = self._rotatewithrightchild(node.left)
        return self._rotatewithleftchild(node)

    def _doublerotateright(self,node):
        node.right = self._rotatewithleftchild(node.right)
        return self._rotatewithrightchild(node)
