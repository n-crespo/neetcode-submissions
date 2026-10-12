# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # now last is at the last twin on the second half
        current = slow
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        res = 0
        while prev:
            print(f"{head.val} + {prev.val}")
            res = max(res, head.val + prev.val)
            prev = prev.next
            head = head.next

        return res