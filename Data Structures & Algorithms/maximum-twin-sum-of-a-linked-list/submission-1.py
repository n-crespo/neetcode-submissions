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

        current = head
        twins = []
        while current != slow:
            twins.append(current.val)
            current = current.next

        i = 1
        res = 0
        while slow:
            res = max(res, twins[-i] + slow.val)
            print(f"new res: {res}")
            slow = slow.next
            i += 1
        return res
