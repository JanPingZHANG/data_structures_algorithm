#!/usr/bin/env python
# encoding: utf-8

def percoDown(ls,pos,n):
    value = ls[pos]
    while True:
        nextpos = pos*2+1
        if nextpos>(n-1):
            break
        if nextpos+1<n and ls[nextpos+1]>ls[nextpos]:
            nextpos = nextpos+1
        if value<ls[nextpos]:
            ls[pos] = ls[nextpos]
            pos = nextpos
        else:
            break
    ls[pos] = value

def swapRefrence(pos1,pos2,ls):
    temp = ls[pos1]
    ls[pos1] = ls[pos2]
    ls[pos2] = temp

def heapSort(ls):
    l = len(ls)
    i = int((l-2)/2)
    while i>=0:
        percoDown(ls,i,l)
        i = i-1
    n = l-1
    while n>0:
        swapRefrence(0,n,ls)
        percoDown(ls,0,n)
        n = n-1

from random import randint
ls = [randint(0,30) for _ in range(20)]
print('source: %s'%ls)
heapSort(ls)
print('sort: %s'%ls)
