# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # the trick is that the LCA is always in between 
        # p and q since we are in a binary search tree. 

        # so we are basically just searching for a node with a value
        # in between p.val and q.val

        # also, notably if the current node is p or q, it is automatically
        # the lowest common ancestor of p and q - anything deeper won't be an
        # ancestor of whatever node we are already on
        
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
            
        