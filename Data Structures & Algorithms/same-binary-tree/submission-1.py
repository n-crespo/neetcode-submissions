# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            for _ in range(len(q1)):
                p = q1.popleft()
                q = q2.popleft()

                if not p and not q:
                    continue
                if not p or not q or p.val != q.val:
                    return False
                q1.append(p.left)
                q1.append(p.right)
                q2.append(q.left)
                q2.append(q.right)
        return True
        