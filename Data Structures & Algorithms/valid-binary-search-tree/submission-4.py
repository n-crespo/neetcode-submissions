# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # depth first search
        # lets use a stack
        stack = [(root, float("-inf"), float("inf"))]
        while stack:
            current, low, high = stack.pop()
            if current:

                if not (low < current.val < high):
                    return False
                    
                stack.append((current.left, low, current.val))
                stack.append((current.right, current.val, high))
        return True