# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # k = 1 --> find smallest value in tree
        # k = 2 --> find 2nd smallest value in tree

        # how to find smallest value? just go all the way down left path
        # how to find next smallest value? go up one and go right!

        # thouguhts:
        # we do DFS first to get smallest, then pop back up. note we also
        # can use the parent node as a result!

        stack = []
        current = root
        n = 0

        while current or stack:
            # push all the way down the left path
            while current:
                stack.append(current)
                current = current.left
            
            # look at the current node (smallest available)
            current = stack.pop()
            n += 1
            if n == k:
                return current.val
            
            # step into the right subtree (the inner while loop will handle its lefts)
            current = current.right
