#!/usr/bin/env python
# encoding: utf-8
from math import log
from random import randint

def shell_sort(ls):
    gap = int(len(ls)/2)
    while gap>0:
        i = gap
        while i<len(ls):
            j = i
            temp = ls[j]
            while j >= gap and ls[j] > ls[j-gap]:
                ls[j-gap] = ls[j]
                j = j-gap
            ls[j] = temp
            i = i+1
        gap = int(gap/2)

'''
nums = [randint(0,100) for _ in range(20)]
print('sources: %s'%nums)
shell_sort(nums)
print('sort: %s'%nums)
t =[5,1]
shell_sort(t)
print(t)
'''

def hibbard_shell(ls):
    k = int(log(len(ls),2))
    gap = 2**k-1
    while gap>0:
        i = gap
        while i<len(ls):
            j=i
            temp = ls[j]
            while j>=gap and temp < ls[j-gap]:
                ls[j] = ls[j-gap]
                j = j-gap
            ls[j] = temp
            i = i+1
        k = k-1
        gap = 2**k-1

nums = [randint(0,100) for _ in range(20)]
print('sources: %s'%nums)
hibbard_shell(nums)
print('sort: %s'%nums)
t =[5,1]
hibbard_shell(t)
print(t)
