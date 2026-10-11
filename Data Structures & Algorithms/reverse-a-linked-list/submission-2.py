# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(prev, head):
            if head == None:
                # print(f"returning: {prev.val}")
                # print(f"next: {prev.next.val}")
                # print(f"next: {prev.next.next.val}")
                return prev
            temp = head.next
            head.next = prev
            return reverse(head, temp)

        return reverse(None, head)