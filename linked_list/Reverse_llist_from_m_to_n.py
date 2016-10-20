'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
        if not head: return None
        if m > n: return 'm is greater than n'
        if m == n: return head

        # Initialize pre node
        dummy_node = ListNode(0)
        dummy_node.next = head
        pre = dummy_node

        for i in range(1, m):
            pre = pre.next
        
        cur = pre.next
        reverse = None
        for i in range(m, n + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next
        
        pre.next.next = cur
        pre.next = reverse

        return dummy_node.next

        