#!/usr/bin/env python
# encoding: utf-8

def mergesort(ls,tmpls,left,right):
    if left<right:
        center = int((left+right)/2)
        mergesort(ls,tmpls,left,center)
        mergesort(ls,tmpls,center+1,right)
        merge(ls,tmpls,left,center,right)

def merge(ls,tmpls,left,center,right):
    leftEnd = center
    rightcursor = center+1
    leftcursor = left
    pos = left
    while leftcursor<=leftEnd and rightcursor<=right:
        if ls[leftcursor]<ls[rightcursor]:
            tmpls[pos] = ls[leftcursor]
            leftcursor+=1
        else:
            tmpls[pos] = ls[rightcursor]
            rightcursor+=1
        pos+=1
    while leftcursor<=leftEnd:
        tmpls[pos] = ls[leftcursor]
        leftcursor+=1
        pos+=1
    while rightcursor<=right:
        tmpls[pos] = ls[rightcursor]
        rightcursor+=1
        pos+=1
    for i in range(left,right+1):
        ls[i] = tmpls[i]

def merge_sort(ls):
    tmpls = []
    tmpls.extend(ls)
    mergesort(ls,tmpls,0,len(ls)-1)

from random import randint
ls = [randint(0,30) for _ in range(20)]
print('source %s'%ls)
merge_sort(ls)
print('sort: %s'%ls)

