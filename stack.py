#!/usr/bin/env python
# encoding: utf-8

class mystack(object):
    def __init__(self):
        self.stacklist = list()
        self.top = -1

    def top(self):
        if self.top < 0:
            raise IndexError('the stack is empty')
        return self.stacklist[self.top]

    def pop(self):
        if self.top < 0:
            raise IndexError('the stack is empty')
        res = self.stacklist[top]
        top = top -1
        return res

    def push(self,elem):
        self.top = self.top + 1
        self.stacklist[top] = elem

