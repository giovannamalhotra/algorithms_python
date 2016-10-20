'''
Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import gc 

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None
        
        pointerA = headA
        pointerB = headB
        
        while pointerA <> pointerB:
            if pointerA: pointerA = pointerA.next
            else: 
                pointerA = headB
                gc.collect()  # clean memory when switching pointers to avoid "memory limit exceeeded" error
            if pointerB: pointerB = pointerB.next
            else: 
                pointerB = headA
                gc.collect()  # clean memory when switching pointers to avoid "memory limit exceeeded" error
            
        
        return pointerA    
                