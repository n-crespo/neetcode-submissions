"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def clone(node):
            # have we looked at this node before? then return clone
            # that we already made
            if node in oldToNew:
                return oldToNew[node]
            
            # we make a copy of the curernt node
            copy = Node(node.val)
            # record that we visited this node
            oldToNew[node] = copy
            # go through all neighbors of original node, 
            # clone them, and add to the clone's neighbors list
            for n in node.neighbors:
                copy.neighbors.append(clone(n))
            
            return copy
        
        # recursive call, only if initial node is non-null
        return clone(node) if node else None
