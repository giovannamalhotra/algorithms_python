'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

def findLongestSubstr(s):

    """
    :type s: str
    :rtype: int
    """

    listStr = list(s)
    n = len(s)
    unique_set = set()
    ans = 0
    i = 0
    j = 0
    while (i < n and j < n):
        #try to extend the range [i, j]
        if listStr[j] not in unique_set:
            unique_set.add(listStr[j])
            j += 1 
            ans = max(ans, j - i)
        
        else:
            unique_set.remove(listStr[i])
            i += 1
        
    
    return ans		


print 'abcabcbb result:'
print findLongestSubstr("abcabcbb")   

print 'bbbbb result:'
print findLongestSubstr("bbbbb")   

print 'pwwkew result:'
print findLongestSubstr("pwwkew")

print '"dvdf result":'
print findLongestSubstr("dvdf")  

