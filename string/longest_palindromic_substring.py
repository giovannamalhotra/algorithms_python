'''
Longest Palindromic Substring

Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
'''

class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''
        
        if len(s) == 1:
            return s
        
        if len(s) == 2 and s[0] == s[1]: 
            return s
        
        max_length = 1
        max_substr = s[0]
        for i in range(1,len(s)):

            p1 = i-1
            p2 = i
            while p1 >=0 and p2 < len(s) and s[p1] == s[p2]:
                if p2 - p1 + 1 > max_length: 
                    max_length = p2 - p1
                    max_substr = s[p1:p2+1]
                p1 -= 1
                p2 += 1


            p1 = i-1
            p2 = i+1
            while p1 >=0 and p2 < len(s) and s[p1] == s[p2]:
                
                if p2 - p1 + 1 > max_length: 
                    max_length = p2 - p1
                    max_substr = s[p1:p2+1]
                p1 -= 1
                p2 += 1
            
        return max_substr       