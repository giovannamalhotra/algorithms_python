#The Euclidean Algorithm for finding GCD(A,B) is as follows:
#
#    If A = 0 then GCD(A,B)=B, since the GCD(0,B)=B, and we can stop.  
#    If B = 0 then GCD(A,B)=A, since the GCD(A,0)=A, and we can stop.  
#    Write A in quotient remainder form (A = BxQ + R)
#    Find GCD(B,R) using the Euclidean Algorithm since GCD(A,B) = GCD(B,R)
#
#Example:
#
#Find the GCD of 270 and 192
#
#    A=270, B=192
#    A <> 0
#    B <> 0
#    Use long division to find that 270/192 = 1 with a remainder of 78. We can write this as: 270 = 192 * 1 +78
#    Find GCD(192,78), since GCD(270,192)=GCD(192,78)


def findGCD(num1, num2):

    if num1 == 0: 
	    return num2
	
    if num2 == 0: 
	    return num1

    remainder = num1 % num2

    return findGCD(num2, remainder)


print findGCD(270, 92)	