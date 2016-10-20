
class Palindrome:
	def longestPalindrome(self, s):
	    """
	    :type s: str
	    :rtype: str
	    """

	    if s is None:
	    	return ''

	    if len(s) == 0:
	        return ''	

	    str_list = list(s)
	    #if s[0] <> s[len_val - 1] 

	    print 'Hello'



p = Palindrome()
p.longestPalindrome('Me')	    