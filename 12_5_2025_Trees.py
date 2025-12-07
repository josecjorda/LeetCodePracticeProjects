# Practicing: Recursion trees
''' I like going to the park pretty often. It's nice to be out in nature, there's something calming about it.
I kind of just want to make a upside down binary tree. I want to search through it with dfs and bfs and have the leaves
change color as the program traverses.
'''

import turtle
from collections import deque

def square(col, loc):
    dist = 20
    pen.goto(loc[1]*dist,loc[0]*dist)
    pen.fillcolor(col)
    pen.begin_fill()
    pen.forward(dist)
    pen.left(90)
    pen.forward(dist)
    pen.left(90)
    pen.forward(dist)
    pen.left(90)
    pen.forward(dist)
    pen.left(90)
    pen.end_fill()

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val
        self.loc = [0,0] #depth, position

def insertLevelOrder(arr, i, n):
    root = None
    # Base case for recursion 
    if i < n:
        root = Node(arr[i]) 
        depth = 0
        while 2**depth <= i+1:
            depth +=1
        depth -=1
        
        pos = 0
        if i != 0:
            pos = i - 2**depth + 1 #idk how this works stumbled into it
            mid = 2**depth//2
            if pos < mid:
                pos = pos - mid
            else:
                pos = pos - (mid - 1)
        root.loc = [depth,pos]
        # insert left child 
        root.l = insertLevelOrder(arr, 2 * i + 1, n)

        # insert right child 
        root.r = insertLevelOrder(arr, 2 * i + 2, n)
        
    return root

def bfs(root):
    if not root:
        return

    queue = deque([root])  # Initialize a queue with the root node

    while queue:
        node = queue.popleft()  # Dequeue the front node
        square("blue", node.loc)
        
        print(node.loc, end="")
        # Enqueue left child if it exists
        if node.l:
            queue.append(node.l)

        # Enqueue right child if it exists
        if node.r:
            queue.append(node.r)


def dfs(root): #preorder
    if not root:
        return None
    square("red", root.loc)
    dfs(root.l)
    dfs(root.r)


arr = []
for i in range(0, 2**4-1):
    arr.append(1)
n = len(arr)
root = None
root = insertLevelOrder(arr, 0, n)
pen = turtle.Turtle()
pen.hideturtle()
bfs(root)
pen.clear
dfs(root)


