'''
Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s_len = len(s)
        if s_len >= 0 and s_len <= 1: return True
        if s_len == 2 and s[0] == s[1]: return True
        
        start = 0
        end = len(s) - 1
        
        while start < end:
            if not s[start].isalnum(): 
                start += 1
                continue
            if not s[end].isalnum(): 
                end -= 1
                continue
            
            if s[start].lower() <> s[end].lower(): return False
            start += 1
            end -= 1
        
        return True    
        
            