#!/usr/bin/env python
# encoding: utf-8

def quick_sort(ls):
    if len(ls)<2:
        return
    left = 0
    right = len(ls)-1
    same = []
    small = []
    bigger = []
    center = int((left+right)/2)
    for item in ls:
        if item>ls[center]:
            bigger.append(item)
        elif item==ls[center]:
            same.append(item)
        else:
            small.append(item)
    quick_sort(small)
    quick_sort(bigger)
    ls.clear()
    ls.extend(small)
    ls.extend(same)
    ls.extend(bigger)

def swap(ls,pos1,pos2):
    tmp = ls[pos1]
    ls[pos1] = ls[pos2]
    ls[pos2] = tmp

def median3(ls,left,right):
    center = int((left+right)/2)
    if ls[right]<ls[left]:
        swap(ls,right,left)
    if ls[center]<ls[left]:
        swap(ls,left,center)
    if ls[center]>ls[right]:
        swap(ls,center,right)
    swap(ls,center,right-1)
    return ls[right-1]

def insertion(ls):
    for i in range(len(ls)):
        tmp = ls[i]
        j = i
        while j>0 and ls[j-1]>tmp:
            ls[j] = ls[j-1]
            j = j-1
        ls[j] = tmp

CUT_OFF = 20
def quicksort(ls,left,right):
    if right-left>CUT_OFF:
        pivot = median3(ls,left,right)
        i = left+1
        j = right-2
        while True:
            while ls[i]<pivot:
                i = i+1
            while ls[j]>pivot:
                j = j-1
            if i>j:
                break
            swap(ls,i,j)
        swap(ls,i,right-1)
        quicksort(ls,left,i-1)
        quicksort(ls,right,i+1)
    else:
        insertion(ls)

from random import randint
ls = [randint(0,1000) for _ in range(100)]
print('source: %s'%ls)
quicksort(ls,0,99)
print('sort: %s'%ls)
for i in range(len(ls)):
    if i>0 and ls[i-1]>ls[i]:
        print('sort error'+'-'*30)
