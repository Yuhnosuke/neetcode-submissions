# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        res_curr = res

        l1_curr, l2_curr = l1, l2

        total, carry = 0, 0

        while l1_curr or l2_curr or carry:
            total = carry

            if l1_curr:
                total += l1_curr.val
                l1_curr = l1_curr.next
            if l2_curr:
                total += l2_curr.val
                l2_curr = l2_curr.next
            
            num = total % 10
            carry = total // 10

            res_curr.next = ListNode(num)
            res_curr = res_curr.next
        return res.next
            
                