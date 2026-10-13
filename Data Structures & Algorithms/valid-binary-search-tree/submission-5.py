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
        
        # important note about BST: we can't just check children against
        # direct parent, need to keep knowledge of ancestor range - we must be
        # within range of all ancestors too. 

        # thus, we set default low/high limits for the root as +- infinity, and 
        # update only upper limit for left, lower for right. (with current value)


        stack = [(root, float("-inf"), float("inf"))]
        while stack:
            current, low, high = stack.pop()
            if current:

                if not (low < current.val < high):
                    return False

                stack.append((current.left, low, current.val))
                stack.append((current.right, current.val, high))

        return True