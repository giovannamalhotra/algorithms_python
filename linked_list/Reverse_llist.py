'''
Reverse Linked List
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head: return None
        cur = head
        prev = None
        
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            
        return prev    