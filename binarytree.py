#!/usr/bin/env python
# encoding: utf-8
from random import randint

class BinaryNode(object):
    def __init__(self,element=None,right=None,left=None):
        self.element = element
        self.right = right
        self.left = left

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def makeEmpty(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def _insert(self,ele,node):
        if node is None:
            return BinaryNode(ele)
        if ele > node.element:
            node.right = self._insert(ele,node.right)
        elif ele < node.element:
            node.left = self._insert(ele,node.left)
        return node
    def insert(self,ele):
        self.root = self._insert(ele,self.root)

    def _print_tree(self,node,pos):
        if node is not None:
            print(' '*pos+str(node.element))
            self._print_tree(node.left,pos-3)
            self._print_tree(node.right,pos+3)
    def print_tree(self,pos):
        self._print_tree(self.root,pos)

    def _iscontains(self,ele,node):
        find = False
        if node is not None:
            if node.element == ele:
                return True
            if ele > node.element:
                find = self._iscontains(ele,node.right)
            elif ele < node.element:
                find = self._iscontains(ele,node.left)
        return find
    def iscontains(self,ele):
        return self._iscontains(ele,self.root)

    def _findMin(self,node):
        if node is None:
            raise ValueError('the node is None in findMin')
        if node.left is not None:
            return self._findMin(node.left)
        else:
            return node
    def findMin(self):
        return self._findMin(self.root).element

    def _findMax(self,node):
        if node is None:
            raise ValueError('the node is None in findMax')
        if node.right is not None:
            return self._findMax(node.right)
        else:
            return node
    def findMax(self):
        return self._findMax(self.root).element

    def _remove(self,ele,node):
        if node is None:
            raise ValueError('the node is not in tree')
        if ele == node.element:
            if node.right is None and node.left is None:
                node = None
            else:
                if node.right is None:
                    find = self._findMax(node.left).element
                    node.left = self._remove(find,node.left)
                else:
                    find = self._findMin(node.right).element
                    node.right= self._remove(find,node.right)
                node.element = find
        else:
            if ele > node.element:
                node.right = self._remove(ele,node.right)
            elif ele < node.element:
                node.left = self._remove(ele,node.left)
        return node
    def remove(self,ele):
        self.root = self._remove(ele,self.root)

tree = BinaryTree()
ls = [randint(0,20) for _ in range(10)]
print(ls)
for i in ls:
    tree.insert(i)
print('-'*30)
tree.print_tree(15)
print('max: %s'%tree.findMax())
print('min: %s'%tree.findMin())
target = ls[randint(0,9)]
print('remove target: %s'%target)
tree.remove(target)
print('target in tree: %s'%tree.iscontains(target))
tree.print_tree(15)
'''
for i in ls:
    print(tree.iscontains(i))
print('+'*30)
for _ in range(10):
    print(tree.iscontains(randint(30,100)))
'''
