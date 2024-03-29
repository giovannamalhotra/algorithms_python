'''
Flatten Binary Tree to Linked List

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        if not root: return None
        self.flatten(root.left)
        self.flatten(root.right)
        
        right = root.right
        
        root.right = root.left
        root.left = None
        
        last_right = root
        while last_right.right:
            last_right = last_right.right
        
        last_right.right = right
                    