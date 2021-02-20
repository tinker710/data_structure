# -*- coding: utf-8 -*-
"""
author： lee
date: 2021-01-27
"""

class tree:
    def __init__(self):
        self.items = [[],[],[]]
    def getTree(self):
        print(self.items)
    def BinaryTree(self,r):
        self.items[0] = r

    def insertLeft(self, newBranch):
        t = self.items.pop(1)
        if len(t) > 1:
            self.items.insert(1,[newBranch,t,[]])
        else:
            self.items.insert(1,[newBranch,[],[]])

    def insertRight(self, newBranch):
        t = self.items.pop(2)
        if len(t) > 1:
            self.items.insert(2,[newBranch,[],t])
        else:
            self.items.insert(2,[newBranch,[],[]])

    def getRootVal(self):
        return self.items[0]

    def setRootVal(self, newVal):
        self.items[0] = newVal

    def getLeftChild(self):
        return self.items[1]

    def getRightChild(self):
        return self.items[2]