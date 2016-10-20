'''
Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        if nums:
            mid_index = int(round(len(nums)/2, 0))
            root = TreeNode(nums[mid_index])
            if mid_index >= 0:
                root.left = self.sortedArrayToBST(nums[:mid_index])
            else:
                root.left = None
            
            if mid_index + 1 < len(nums):    
                root.right = self.sortedArrayToBST(nums[mid_index + 1:])        
            else:
                root.right = None
                
            return root
        else:
            return None