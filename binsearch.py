#!/usr/bin/env python3

import random
from time import time

class Node:

  def __init__ (self, value):
    """ create a binary node """
    self.value = value
    self.left = None
    self.right = None

  def add (self, val):
    if self.value is not None:
    # recursive add node ensures node is added at correct location 

      if val <= self.value:

        if self.left: self.left.add(val)
        else: self.left = Node(val)

      else:
        if self.right: self.right.add(val)
        else: self.right = Node(val)

    else: self.value = val


class Tree:
  def __init__ (self):
    """ start a binary tree """
    self.root = None

  def add (self, value):

    if self.root == None:     
      self.root = Node(value)

    else:
      self.root.add(value) # invokes Node's recursive add

  def largest (self):
      node = self.root
      while node.right: node=node.right
      return node.value

  def smallest (self):
      node = self.root
      if not node.left: return node.value
      while node.left: node=node.left
      return node.value

  def contains (self, target):
    """Check whether BST contains target value"""
    node = self.root

    while node:
      if target == node.value: return True
      if target < node.value: node = node.left
      else: node = node.right
    return False 


def testbt(from_list):
  bt = Tree()
  [bt.add(i) for i in from_list]
  return bt

A = [3,4,6, 7, 99, 23, 42]
bt = testbt(A)

print ("A = ",A)
print ("largest = ",bt.largest())
print ("smallest = ",bt.smallest())


# find the smallest
# find the largest

def performance():
    n = 1024
    while n < 65536:
      bt = Tree()
      for i in range(n):
          bt.add(random.randint(1,n))

      now = time()
      bt.contains (random.randint(1,n))
      print (n, (time() - now)*1000000)
      n *= 2
