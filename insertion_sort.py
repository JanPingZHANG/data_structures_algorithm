#!/usr/bin/env python
# encoding: utf-8
from random import randint

def insertionsort(ls):
    for i in range(len(ls)):
        j = i
        temp = ls[j]
        while j>0 and temp < ls[j-1]:
            ls[j] = ls[j-1]
            j = j-1
        ls[j] = temp

ls = [randint(0,20) for _ in range(10)]
print('source: %s'%ls)
insertionsort(ls)
print('sort: %s'%ls)

