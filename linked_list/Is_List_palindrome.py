'''
Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head: return True  # If linked list is empty then return True
        if not head.next: return True # if LinkedList has only one element then return True
        if not head.next.next and head.val == head.next.val: return True # If linked list has 2 elements and those two elements are the same then return True
        
        
        current = head
        middle = head
        counter = 1
        prev = None
        
        # FInd Middle. For every two positions, middle moves only one position
        while current and current.next:
            current = current.next.next
            next_middle = middle.next
            middle.next = prev            
            prev = middle
            middle = next_middle
            counter += 2
        
        if not current:  #counter jumped to null, need to decrease counter
            counter -= 1

        # If counter is even, it means middle is next element to middle. Middle should be considered as part of second half                
        if  counter%2 == 0:
            half1 = prev
            half2 = middle
        else:
        #Counter is odd, so middle is not part of second half        
            half1 = prev
            half2 = middle.next
            
        # Traverse the two half linked list and compare values one by one    
        while half1 and half2 and half1.val == half2.val:
            print half1.val
            print half2.val
            half1 = half1.next
            half2 = half2.next
            
        return half1 == None and half2 == None    
        