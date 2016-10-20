from collections import defaultdict


def isAnagramPalindrome(str):

    d = defaultdict(int)

    for l in str:
		#print l
	    d[l] += 1

    
    foundOddCount = False
    for k, v in d.iteritems():
        if v%2 <> 0:
            if foundOddCount:
                return False
            else:
                foundOddCount = True	

    return True



print isAnagramPalindrome('racecar')