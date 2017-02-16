#!/usr/bin/env python
# encoding: utf-8

class BinaryHeap(object):
    def __init__(self,ls=None):
        self.arraylist = [None,]
        if ls is not None:
            self.arraylist.extend(ls)
        self.currentsize = len(self.arraylist)-1
        self._buildHeap()

    def insert(self,x):
        pos = ++self.currentsize
        self.arraylist.append(None)
        while x<self.arraylist[int(pos/2)] and pos>1 :
            self.arraylist[pos] = self.arraylist[int(pos/2)]
            pos = int(pos/2)
        self.arraylist[pos] = x

    def findMin(self):
        return self.arraylist[self.currentsize]

    def deleteMin(self):
        if self.currentsize==0:
            raise IndexError('the binaryHeap is empty')
        self.arraylist[1] = self.arraylist.pop()
        self.currentsize = self.currentsize-1
        self._percolateDown(1)

    def _buildHeap(self):
        i = int(self.currentsize/2)
        while i>0:
            self._percolateDown(i)
            i = i-1

    def _percolateDown(self,pos):
        origin=self.arraylist[pos]
        while True:
            if pos*2 > self.currentsize:
                break
            if origin>self.arraylist[pos*2]:
                self.arraylist[pos]=self.arraylist[pos*2]
                pos=pos*2
            elif pos*2+1<=self.currentsize and origin>self.arraylist[pos*2+1]:
                self.arraylist[pos]=self.arraylist[pos*2+1]
                pos=pos*2+1
            else:
                break
        self.arraylist[pos]=origin

    def isEmpty(self):
        return self.currentsize==0
    def makeEmpty(self):
        self.arraylist.clear()
        self.arraylist.append(None)
        self.currentsize=0

